import subprocess
import json
from query import get_contexts

def send_prompt(query_text: str, model="qwen2:1.5b"):
    contexts = get_contexts(query_text)

    # Combine the contexts
    context_text = "\n\n---\n\n".join(contexts)
    print(context_text)
    prompt = f"{context_text}\n\nExplain what the user was doing at the time this was opened: {query_text}"

    # Using curl to send the request to the LLM
    command = [
        'curl',
        '-X', 'POST',
        'http://localhost:11434/api/generate',
        '-d', json.dumps({"model": model, "prompt": prompt, "stream": False}),
        '-H', 'Content-Type: application/json'
    ]
    try:
        response = subprocess.run(command, capture_output=True, text=True, check=True)
        response_json = json.loads(response.stdout)
        response_text = response_json.get('response', 'No response from the model')
        print(f"Response: {response_text}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")
        print(f"Command output: {e.output}")

if __name__ == "__main__":
    query_text = input("Enter your question: ")
    model = input("Enter the model you want to use (default is 'qwen2'): ") or "qwen2:1.5b"
    send_prompt(query_text, model)
