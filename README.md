# jinaai-demo

## Introduction

In light of concerns surrounding Windows' new 'Windows Recall' feature, which records screens and performs OCR,  we present an open-source alternative. Our tool offers the same functionality while ensuring user data remains local.
Windows Recall on Windows laptops continuously records screens and performs OCR. Despite the embedded NPUs in these devices, users worry about mandatory cloud data transmission. This worry is well-founded, as transmitting data to the cloud involves risks such as unauthorized access, data breaches, and potential misuse of personal information. To address these concerns, we have created an open-source tool that keeps all data processing local.
Our solution prioritizes user privacy and security. By keeping all data processing on the user's device, we eliminate the need for any data to be transmitted to external servers. This approach ensures that users have full control over their data, significantly reducing the risk of unauthorized access or misuse.
Leveraging the Power of JinaAI
Our project showcases the power of open-source tools in creating robust, privacy-conscious alternatives to proprietary solutions. By leveraging libraries like PyAutoGUI, DocTR, Ollama, and JinaAI, we provide a feature-rich solution that meets user needs without compromising privacy.
JinaAI plays a crucial role in our implementation by providing high-quality embedding and re-ranking capabilities. Here's how:
Embedding Model: JinaAI's embedding model creates efficient and high-quality vector representations of the text extracted from screenshots. These embeddings capture the semantic meaning of the text, enabling precise and relevant information retrieval.
Reranker Model: The reranker model from JinaAI enhances the accuracy of the retrieved data. After performing a standard semantic search, the reranker model re-evaluates the results to select the most relevant chunks. This ensures that the information presented to the user is not only contextually appropriate but also the most pertinent to their query.
The combination of JinaAI’s embedding and reranking models significantly boosts the performance of our tool. These models are designed to work seamlessly together, providing an efficient and effective method for processing and retrieving data.

## Project Overview

Our implementation leverages several open-source tools to replicate the functionality of Windows Recall without the need to send data to external servers. Here's a breakdown of the components:
* PyAutoGUI: This tool is used for capturing screenshots at regular intervals.
* DocTR: A state-of-the-art OCR tool that performs text recognition on the captured images.
* Ollama: Used for local LLM’s.
* JinaAI: JinaAI's embedding model and reranker enhances the accuracy of the retrieved data.
* ChromaDB: A database used to store embeddings for efficient retrieval.

## Setup Guide
Clone the repository (data-max-hq/open-recall)
cd into /open-recall
pip install pyautogui
In the terminal run ‘make build’
In the terminal run ‘make run’
After a couple of minutes then head over to "localhost:9876"
In "ADD LLM" type out the LLM you want to use (we recomend qwen2:1.5b or qwen2:0.5b) and press "Add LLM"

## Functionality
Run "screenshot-desktop.py" to start capturin the screen
Query ChromaDB: Test the database to retrieve relevant pieces of context for a specific query.
LLM Prompt: Pass a query to QWEN2:1.5b to get an explanation of what the user was doing based on the retrieved context.
Summary
In summary, our open-source alternative to Windows Recall offers a secure, private, and efficient way to continuously record screens and perform OCR, ensuring that all data remains under the user's control. By leveraging the high-quality embedding and reranking models from JinaAI, we enhance the accuracy and relevance of the information retrieved, providing users with a powerful and privacy-conscious solution. This project demonstrates the potential of open-source tools to address privacy concerns while delivering robust functionality.


