# Open-Memory

## Setup Guide
* Clone the repository (data-max-hq/open-memory)
* cd into /open-memory
* pip install pyautogui
* In the terminal run ‘make build’
* In the terminal run ‘make run’
* After a couple of minutes then head over to "localhost:8080"
* In "ADD LLM" type out the LLM you want to use (we recomend qwen2:1.5b or qwen2:0.5b) and press "Add LLM"

## Functionality
Run "screenshot-desktop.py" to start capturin the screen

  
Query ChromaDB: Test the database to retrieve relevant pieces of context for a specific query.

  
LLM Prompt: Pass a query to QWEN2:1.5b to get an explanation of what the user was doing based on the retrieved context.

  
## Summary

  
In summary, our open-source alternative to Windows Recall offers a secure, private, and efficient way to continuously record screens and perform OCR, ensuring that all data remains under the user's control. By leveraging the high-quality embedding and reranking models from JinaAI, we enhance the accuracy and relevance of the information retrieved, providing users with a powerful and privacy-conscious solution. This project demonstrates the potential of open-source tools to address privacy concerns while delivering robust functionality.


