# Flask Task Queue

This is a Dockerized Python application using Flask, Redis, and a background worker with Docker Compose.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose

### Installing

1. Clone the repository

git clone https://github.com/yourusername/flask-task-queue.git

2. Navigate to the project directory

cd flask-task-queue

3. Build and run the Docker containers

docker-compose up --build


## Usage

The application has two parts: a web server and a background worker.

- The web server is a Flask application that accepts tasks at the `/task` endpoint via POST requests.
- The background worker processes tasks from a Redis queue.

## Deployment

You can push this application to your GitHub repository and then use AWS Elastic Beanstalk Multi-Container Docker environment for deployment.
