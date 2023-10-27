# Terraform AWS Web Application Infrastructure

## Overview

This Terraform project provides infrastructure as code (IAC) for deploying a scalable web application on Amazon Web Services (AWS). It includes a Virtual Private Cloud (VPC), an EC2 instance, security groups, and an Application Load Balancer (ALB) to create a highly available and resilient environment for your web application.

## Features

- **Scalable Web Application**: The infrastructure is designed to host a web application that can easily handle traffic spikes and scale horizontally as needed.

- **High Availability**: The application is deployed across multiple availability zones to ensure high availability and fault tolerance.

- **Security Groups**: Security groups are used to control inbound and outbound traffic to the EC2 instance, ensuring the application's security.

- **Load Balancing**: The ALB distributes incoming traffic to multiple instances, improving application availability and performance.

- **Customizable**: You can easily customize the infrastructure by adjusting the provided variables and settings.

## Prerequisites

Before you begin, ensure you have the following prerequisites:

- [Terraform](https://www.terraform.io/downloads.html)
- [AWS CLI](https://aws.amazon.com/cli/)
- An AWS account with appropriate access credentials.
- An SSH key pair for EC2 instances.

## Getting Started

1. **Clone the Repository**:

   ```shell
   git clone <repository-url>
   cd terraform-aws-web-app
Update Configuration:

Navigate to the ec2 directory and update the variables.tf file with your desired configuration settings. Key parameters include:
ami_id: The ID of the Amazon Machine Image (AMI) for the EC2 instance.
instance_type: The type of EC2 instance to launch.
key_name: The name of the SSH key pair to use for EC2 instances.
subnet_id: The ID of the subnet where the EC2 instance will be launched.
security_groups: A list of security group IDs to associate with the EC2 instance.
You can modify other variables as needed for your use case.
Initialize Terraform:

In each module directory (vpc, ec2, alb), run the following command to initialize Terraform:

shell
Copy code
terraform init
Apply Configuration:

Apply the configuration for each module:

shell
Copy code
cd vpc
terraform apply
cd ../ec2
terraform apply
cd ../alb
terraform apply
Confirm Changes:

Follow the prompts and confirm the changes when prompted.
Outputs
This project provides useful outputs that give you important information about the deployed resources. You can retrieve this information using Terraform outputs. For example:

In the ec2 module directory, you can run the following command to get the EC2 instance ID:

shell
Copy code
terraform output ec2_instance_id
You can use these outputs to interact with your AWS resources and to integrate them with your web application.

Customization
The infrastructure is highly customizable. You can adjust the variables in the variables.tf files within each module to meet your specific requirements. Make sure to apply changes consistently across the modules as needed.

Cleanup
When you're done with this project, it's essential to clean up your AWS resources to avoid incurring unnecessary charges. To destroy the infrastructure, follow these steps:

In each module directory (vpc, ec2, alb), run the following command:

shell
Copy code
terraform destroy
Follow the prompts and confirm the destruction of the resources.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
This project was created to help you deploy a scalable and highly available web application infrastructure on AWS. If you find it useful, please consider sharing and contributing to the open-source community.

Happy coding!