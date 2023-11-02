# Custom Kubernetes Scheduler

This project demonstrates the creation of a Custom Kubernetes Scheduler using a Python wrapper around the kube-scheduler Go binary. The custom scheduler can apply custom scheduling rules to pod assignments, such as resource requirements, times of day, and more. Please note that this example simplifies the scheduler's functionality for demonstration purposes.

## Prerequisites

Before using the custom scheduler, ensure you have the following prerequisites:

- A running Kubernetes cluster.
- `kubectl` command-line tool configured to access your cluster.
- Docker installed on your machine for building the scheduler image.

## Project Structure

The project consists of the following components:

1. **scheduler.py**: Python script that wraps the `kube-scheduler` Go binary and applies custom scheduling rules.

2. **Dockerfile**: Used to containerize the custom scheduler.

3. **scheduler-deployment.yaml**: Kubernetes Deployment manifest to deploy the custom scheduler.

4. **scheduler-service-account.yaml**: Kubernetes ServiceAccount for the custom scheduler.

## Usage

1. Build the custom scheduler Docker image:

   docker build -t your-docker-hub-username/custom-scheduler:latest .
Deploy the custom scheduler to your Kubernetes cluster:

kubectl apply -f scheduler-service-account.yaml
kubectl apply -f scheduler-deployment.yaml
The custom scheduler is now running as a Kubernetes Deployment, applying custom scheduling rules to pod assignments.

Customization
Customize the scheduler.py script to implement your desired scheduling logic. You can modify the Go binary's flags, policies, and behaviors according to your specific requirements.

Cleanup
To remove the custom scheduler and associated resources:

Delete the custom scheduler Deployment:

kubectl delete -f scheduler-deployment.yaml
Optionally, delete the custom scheduler ServiceAccount:

kubectl delete -f scheduler-service-account.yaml

License
This project is provided under the MIT License - see the LICENSE file for details.

You can use this `README.md` as part of your project's documentation and tailor it to your specific needs.