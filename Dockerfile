# Use the DocTR image as the base image
FROM ghcr.io/mindee/doctr:torch-py3.9.18-gpu-2024-05

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the working directory
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Create directories for screenshots and chroma if they don't exist
RUN mkdir -p /app/screenshots /app/chroma

#Ollama
RUN curl -fsSL https://ollama.com/install.sh | sh
RUN ollama pull qwen2:1.5b

# Expose ports
EXPOSE 9876
EXPOSE 11434

# Command to run the Flask app
CMD ["python3", "app.py"]
