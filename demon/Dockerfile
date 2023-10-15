# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the entire project directory into the container
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r api/requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable (you may customize this)
ENV NAME="WhatsAppAPI"

# Run your API script as the entry point
CMD ["python", "-m", "api.whatsapp_api"]
