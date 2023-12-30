# Advanced E-commerce Microservices Platform

This project demonstrates a microservices-based e-commerce platform with advanced security measures and infrastructure management using Docker, Terraform, and Python web frameworks.

## Directory Structure

- `authentication_service/`: Contains the FastAPI-based authentication service.
- `product_service/`: Contains the Flask-based product service.
- `terraform/`: Contains Terraform configuration files for infrastructure deployment.
- `security/`: Contains Linux scripts for basic server security.

## Getting Started

To start using this project, follow the steps below:

### Prerequisites

- Docker
- Terraform
- Python

### Setup

1. Clone the repository.
2. Navigate to `authentication_service/` and `product_service/` directories and build the Docker images.
3. Deploy infrastructure using Terraform in the `terraform/` directory.

## Docker and Services

### Authentication Service

- Utilizes FastAPI and JWT for secure authentication.

### Product Service

- Utilizes Flask for managing product functionalities.

## Terraform Configuration

The `main.tf` and `variables.tf` files in the `terraform/` directory define AWS resources and configurations for deployment.

## Security Scripts

### Firewall Configuration

Run `firewall_configuration.sh` to set up basic firewall rules using iptables.

### Brute Force Protection

Run `brute_force_protection.sh` to configure fail2ban for protecting against brute-force attacks.

## Authors

* Simardeep Singh

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
