# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster as builder

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install pip in a separate layer for better caching
RUN pip install --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Use multi-stage builds to create a clean, final image
FROM python:3.8-slim-buster

# Copy the Python installation from the builder stage
COPY --from=builder /usr/local /usr/local

# Set the working directory in the container to /app
WORKDIR /app

# Copy the application from the builder stage
COPY --from=builder /app /app

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python", "app.py"]