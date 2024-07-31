### Open-Memory

## Introduction

In response to growing privacy concerns and Microsoft's "Windows Recall" feature, which records and analyzes screen activities by transmitting data to the cloud, we have developed an open-source pilot that offers similar functionality without compromising user privacy.

## Usage Flow

- The user runs `screenshot-desktop.py` whenever they want to start recording their screens.
- The extracted text from the screenshots is processed by the DocTR OCR tool and stored in the ChromaDB vector database, along with their corresponding embeddings generated by the JinaAI embedding model.
- When the user has a query or needs to retrieve relevant information, they can input their request into `LLM Prompt`.
- The query is then processed by the JinaAI reranker model, which retrieves the most relevant text chunks from the ChromaDB database based on the semantic similarity of the embeddings.
- The retrieved information is presented to the user, providing them with the necessary context and insights without ever leaving their local device.
- This approach ensures that all data processing and storage remain under the user's control, eliminating the risks associated with cloud-based solutions and empowering users to maintain their privacy.

## Setup Guide

### Prerequisites

- Python 3.11 
- Docker
- Docker Compose
- Make

### Installation Steps

1. **Install Docker:**

   Follow the official Docker installation guide for your operating system:
   - [Docker for Windows](https://docs.docker.com/docker-for-windows/install/)
   - [Docker for macOS](https://docs.docker.com/docker-for-mac/install/)
   - [Docker for Linux](https://docs.docker.com/engine/install/)

   After installing Docker, ensure it's running correctly by executing:
   ```sh
   docker --version
   ```


2. **Install Make:**

   Depending on your operating system, install Make:

   - **Windows:** Install [Make for Windows](http://gnuwin32.sourceforge.net/packages/make.htm).
   - **macOS:** Use Homebrew (if not installed, follow [Homebrew installation](https://brew.sh/)):
     ```sh
     brew install make
     ```
   - **Linux:** Install Make using your distribution's package manager:
     ```sh
     sudo apt-get install build-essential  # For Debian/Ubuntu
     sudo yum group install 'Development Tools'  # For CentOS/RHEL
     ```

3. **Clone the Repository and Install Python Dependencies:**

   ```sh
   git clone https://github.com/data-max-hq/open-memory.git
   cd open-memory
   pip install pyautogui
   ```

4. **Build and Run the Docker Containers:**

   ```sh
   make build
   make run
   ```

5. **Access the Application:**

   After the containers are up and running, open your web browser and navigate to:
   ```
   http://localhost:8080
   ```

   In the "ADD LLM" section, type the LLM you want to use (we recommend `qwen2:1.5b` or `qwen2:0.5b`) and press "Add LLM".

## Functionality

- **Run `screenshot-desktop.py` to start capturing the screen.**
- **Query ChromaDB:** Test the database to retrieve relevant pieces of context for a specific query.
- **LLM Prompt:** Pass a query to QWEN2:1.5b to get an explanation of what the user was doing based on the retrieved context.
