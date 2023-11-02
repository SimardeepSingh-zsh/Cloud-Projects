# Use a base image that includes Python and Kubernetes binaries
FROM ubuntu:latest

# Install any required packages and dependencies
RUN apt-get update -y && apt-get install -y \
    python3 \
    kubectl \
    # Add other dependencies as needed
    && rm -rf /var/lib/apt/lists/*

# Copy the Python scheduler script and any policy configuration
COPY scheduler.py /
COPY policy-config.json /

# Make the Python script executable
RUN chmod +x /scheduler.py

# Set the entry point to run the Python scheduler script
ENTRYPOINT ["/scheduler.py"]