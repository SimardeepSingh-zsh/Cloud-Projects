# Use a Python base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy app files
COPY . /app/

# Set permissions and run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
