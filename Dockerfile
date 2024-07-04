# Use the DocTR image as the base image
FROM ghcr.io/mindee/doctr:torch-py3.9.18-gpu-2024-05

# Set the working directory inside the container
WORKDIR /app

# Copy the project files into the working directory
COPY . /app

# Install Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Install supervisor
RUN apt-get update && apt-get install -y supervisor

# Create directories for screenshots and chroma if they don't exist
RUN mkdir -p /app/screenshots /app/chroma

# Copy supervisor configuration file
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose ports
EXPOSE 8080

# Command to run the supervisor
CMD ["/usr/bin/supervisord"]
