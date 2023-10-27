variable "ami_id" {
  description = "The ID of the Amazon Machine Image (AMI) to use for the EC2 instance."
  type        = string
  default     = "ami-0c55b159cbfafe1f0"  # Replace with your desired default AMI
}

variable "instance_type" {
  description = "The type of EC2 instance to launch."
  type        = string
  default     = "t2.micro"
}

variable "key_name" {
  description = "The name of the SSH key pair to use for EC2 instances."
  type        = string
}

variable "subnet_id" {
  description = "The ID of the subnet where the EC2 instance will be launched."
  type        = string
}

variable "security_groups" {
  description = "A list of security group IDs to associate with the EC2 instance."
  type        = list(string)
}

# Add more variables as needed for your use case.
