provider "aws" {
  region = "ca-central-1"  # Update with your desired region
}

resource "aws_vpc" "example_vpc" {
  cidr_block = "10.0.0.0/16"
  enable_dns_support = true
  enable_dns_hostnames = true
  tags = {
    Name = "example-vpc"
  }
}

resource "aws_subnet" "example_subnet" {
  count = 2
  vpc_id = aws_vpc.example_vpc.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "us-east-1a"  # Update with desired availability zones
  map_public_ip_on_launch = true
}

resource "aws_security_group" "example_sg" {
  name        = "example-sg"
  description = "Example security group"
  vpc_id      = aws_vpc.example_vpc.id

  // Define inbound and outbound rules here
}

resource "aws_internet_gateway" "example_igw" {
  vpc_id = aws_vpc.example_vpc.id
}
