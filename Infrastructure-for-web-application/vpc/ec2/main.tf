provider "aws" {
  region = "ca-central-1"  # Update with your desired region
}

resource "aws_key_pair" "example_keypair" {
  key_name   = "example-keypair"
  public_key = file("~/.ssh/id_rsa.pub")  # Update with your SSH public key file
}

resource "aws_instance" "example_ec2" {
  ami           = "ami-0c55b159cbfafe1f0"  # Update with your desired AMI
  instance_type = "t2.micro"
  key_name      = aws_key_pair.example_keypair.key_name
  subnet_id     = aws_subnet.example_subnet[0].id
  security_groups = [aws_security_group.example_sg.id]

  // Add additional configurations (e.g., user data, instance tags) here
}
