from flask import Flask, render_template, request, redirect, url_for, send_from_directory, abort
import threading
from testfull import capture_analyze_and_embed  # Assuming this is a module you have
from query import QueryRAG  # Assuming this is the QueryRAG class defined earlier
import os

# Create Flask App
app = Flask(__name__)

# Global Variables
recording_active = False
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
    global screenshot_counter
    return render_template('index.html', counter=screenshot_counter, results=[])

@app.route('/toggle-recording', methods=['POST'])
def toggle_recording():
    global recording_active, screenshot_thread
    recording_active = not recording_active
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
    return render_template('index.html', results=results, counter=screenshot_counter)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9876, debug=False)
