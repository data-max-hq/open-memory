# Open-Memory

## Setup Guide
* Clone the repository (data-max-hq/open-memory)
* cd into /open-memory
* pip install pyautogui
* In the terminal run ‘make build’
* In the terminal run ‘make run’
* After a couple of minutes then head over to "localhost:8080"
* In "ADD LLM" type out the LLM you want to use (we recomend qwen2:1.5b or qwen2:0.5b) and press "Add LLM"

## Usage Flow:

The user runs ‘screenshot-desktop.py’ whenever they want to start recording their screens

  
The extracted text from the screenshots is processed by the DocTR OCR tool and stored in the ChromaDB vector database, along with their corresponding embeddings generated by the JinaAI embedding model.

  
When the user has a query or needs to retrieve relevant information, they can input their request into ‘LLM Prompt’.

  
The query is then processed by the JinaAI reranker model, which retrieves the most relevant text chunks from the ChromaDB database based on the semantic similarity of the embeddings.

  
The retrieved information is presented to the user, providing them with the necessary context and insights without ever leaving their local device.

  
This approach ensures that all data processing and storage remain under the user's control, eliminating the risks associated with cloud-based solutions and empowering users to maintain their privacy.

  

## Functionality
Run "screenshot-desktop.py" to start capturin the screen

  
Query ChromaDB: Test the database to retrieve relevant pieces of context for a specific query.

  
LLM Prompt: Pass a query to QWEN2:1.5b to get an explanation of what the user was doing based on the retrieved context.

  
## Summary

  
In summary, our open-source alternative to Windows Recall offers a secure, private, and efficient way to continuously record screens and perform OCR, ensuring that all data remains under the user's control. By leveraging the high-quality embedding and reranking models from JinaAI, we enhance the accuracy and relevance of the information retrieved, providing users with a powerful and privacy-conscious solution. This project demonstrates the potential of open-source tools to address privacy concerns while delivering robust functionality.


