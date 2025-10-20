FROM python:3.11-slim

WORKDIR /app

# Copy files from app directory
COPY app/ /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Mount data directory
VOLUME ["/data"]

# Run script
CMD ["python", "main.py"]
