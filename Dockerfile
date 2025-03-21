# Use Python 3.12 slim image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies including ffmpeg & git
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    ffmpeg \
 && rm -rf /var/lib/apt/lists/*

# Copy requirements file first to take advantage of Docker cache
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app into the container
COPY . /app/

# Expose FastAPI port (usually 8000)
EXPOSE 8000

