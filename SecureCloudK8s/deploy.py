import os
import subprocess
import logging

logging.basicConfig(level=logging.INFO)

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        logging.error(f'Error executing {command}. Error: {stderr.decode()}')
        return False

    logging.info(stdout.decode())
    return True

def deploy():
    # Build Docker image
    if not run_command(["docker", "build", "-t", "my-python-app", "."]):
        logging.error('Failed to build Docker image.')
        return

    # Push Docker image to registry
    if not run_command(["docker", "push", "my-python-app"]):
        logging.error('Failed to push Docker image to registry.')
        return

    # Apply Kubernetes manifests
    if not run_command(["kubectl", "apply", "-f", "k8s/"]):
        logging.error('Failed to apply Kubernetes manifests.')
        return

    logging.info('Deployment successful.')

if __name__ == "__main__":
    deploy()