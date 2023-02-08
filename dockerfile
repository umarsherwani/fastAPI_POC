# Use an official Python runtime as the base image
FROM python:3.9-alpine

# Set the working directory in the container to /app
WORKDIR /pymango

# Copy the current directory contents into the container at /app
COPY . /pymango

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Expose port 8000 for the FastAPI application to listen on
EXPOSE 8000

# Define the command to run the FastAPI application
CMD ["uvicorn", "index:app", "--host", "0.0.0.0", "--port", "8000"]
