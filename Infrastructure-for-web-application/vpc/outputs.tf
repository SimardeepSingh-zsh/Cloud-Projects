output "ec2_instance_id" {
  description = "The ID of the EC2 instance."
  value       = aws_instance.example_ec2.id
}

output "ec2_private_ip" {
  description = "The private IP address of the EC2 instance."
  value       = aws_instance.example_ec2.private_ip
}

output "ec2_public_ip" {
  description = "The public IP address of the EC2 instance."
  value       = aws_instance.example_ec2.public_ip
}

# Add more outputs as needed for your use case.
