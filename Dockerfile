# Use a lightweight Python base image
FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /app

# Install build tools needed for installing Python packages
RUN apk add --no-cache gcc musl-dev

# Copy only requirements first (better caching)
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app folder into the container
COPY app/ .

# Expose port 3000
EXPOSE 3000

# Run your Flask app
CMD ["python", "main.py"]
