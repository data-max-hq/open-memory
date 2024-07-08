# Open-Memory

## Introduction:

In response to growing privacy concerns and Microsoft's "Windows Recall" feature, which records and analyzes screen activities by transmitting data to the cloud, we have developed an open-source pilot that offers similar functionality without compromising user privacy.

## Usage Flow:

The user runs ‘screenshot-desktop.py’ whenever they want to start recording their screens

  
The extracted text from the screenshots is processed by the DocTR OCR tool and stored in the ChromaDB vector database, along with their corresponding embeddings generated by the JinaAI embedding model.

  
When the user has a query or needs to retrieve relevant information, they can input their request into ‘LLM Prompt’.

  
The query is then processed by the JinaAI reranker model, which retrieves the most relevant text chunks from the ChromaDB database based on the semantic similarity of the embeddings.

  
The retrieved information is presented to the user, providing them with the necessary context and insights without ever leaving their local device.

  
This approach ensures that all data processing and storage remain under the user's control, eliminating the risks associated with cloud-based solutions and empowering users to maintain their privacy.



## Setup Guide
* Clone the repository (data-max-hq/open-memory)
  ```
  cd /open-memory
  pip install pyautogui
  make build
  make run
  ```
* After a couple of minutes then head over to "localhost:8080"
* In "ADD LLM" type out the LLM you want to use (we recomend qwen2:1.5b or qwen2:0.5b) and press "Add LLM"

  

## Functionality
Run "screenshot-desktop.py" to start capturin the screen

  
Query ChromaDB: Test the database to retrieve relevant pieces of context for a specific query.

  
LLM Prompt: Pass a query to QWEN2:1.5b to get an explanation of what the user was doing based on the retrieved context.
