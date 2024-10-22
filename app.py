from flask import Flask, render_template, request, redirect, url_for, send_from_directory, abort
import threading
import subprocess
import json
from OCRProc import capture_analyze_and_embed  # Assuming this is a module you have
from query import QueryRAG, get_contexts  # Assuming this is the QueryRAG class defined earlier and get_contexts
import os
import requests  # Add requests library for making HTTP requests

# Create Flask App
app = Flask(__name__)

# Global Variables
recording_active = True
screenshot_counter = 0
screenshot_thread = None

# Create Query Handler
query_handler = QueryRAG()

def take_screenshots():
    global screenshot_counter
    while recording_active:
        capture_analyze_and_embed()
        screenshot_counter += 1

@app.route('/')
def index():
    global screenshot_counter, recording_active
    return render_template('index.html', counter=screenshot_counter, recording_active=recording_active, results=[], prompt_response=None)

@app.route('/toggle-recording', methods=['POST'])
def toggle_recording():
    global recording_active, screenshot_thread
    if recording_active:
        screenshot_thread = threading.Thread(target=take_screenshots)
        screenshot_thread.start()
    else:
        if screenshot_thread:
            screenshot_thread.join()
    return redirect(url_for('index'))

@app.route('/query', methods=['POST'])
def query():
    query_text = request.form.get('query_text')
    results = []
    if query_text:
        results = query_handler.query(query_text)
        results = [(context, doc_id.replace("\\", "/").split("/")[-1]) for context, doc_id in results]
    return render_template('index.html', results=results, counter=screenshot_counter, recording_active=recording_active, prompt_response=None)

def send_prompt(query_text: str, model="qwen2:1.5b"):
    contexts = get_contexts(query_text)

    # Combine the contexts
    context_text = "\n\n---\n\n".join(contexts)
    print(context_text)
    prompt = f"{context_text}\n\nExplain what the user was doing at the time this was opened: {query_text}"

    # Using requests to send the request to the LLM
    url = 'http://ollama-service:11434/api/generate'
    headers = {'Content-Type': 'application/json'}
    payload = {'model': model, 'prompt': prompt, 'stream': False}
    
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        response_json = response.json()
        response_text = response_json.get('response', 'No response from the model')
        print(f"Response: {response_text}")
        return response_text
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
        return "An error occurred while processing the request."

@app.route('/handle_prompt', methods=['POST'])
def handle_prompt():
    prompt_text = request.form.get('prompt_text')
    model = request.form.get('model', 'qwen2:1.5b')
    prompt_response = send_prompt(prompt_text, model)
    return render_template('index.html', counter=screenshot_counter, recording_active=recording_active, results=[], prompt_response=prompt_response)

@app.route('/screenshots/<path:filename>')
def get_screenshot(filename):
    try:
        # Print debug information
        print(f"Requested filename: {filename}")
        full_path = os.path.join('screenshots', filename)
        print(f"Full path to file: {full_path}")
        if not os.path.exists(full_path):
            print(f"File {full_path} does not exist")
            abort(404)
        return send_from_directory('screenshots', filename)
    except Exception as e:
        print(f"An error occurred: {e}")
        abort(500)

@app.route('/add_llm', methods=['POST'])
def add_llm():
    llm_text = request.form['llm_text']
    data = {"name": llm_text}
    try:
        response = requests.post('http://ollama-service:11434/api/pull', json=data)
        if response.status_code == 200:
            print('LLM added successfully')
        else:
            print(f"Failed to add LLM: {response.status_code}, {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
