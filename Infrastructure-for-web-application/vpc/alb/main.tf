provider "aws" {
  region = "ca-central-1"  # Update with your desired region
}

resource "aws_lb" "example_alb" {
  name               = "example-alb"
  internal           = false
  load_balancer_type = "application"
  subnets            = [aws_subnet.example_subnet[0].id, aws_subnet.example_subnet[1].id]

  enable_deletion_protection = false
}

resource "aws_lb_target_group" "example_target_group" {
  name     = "example-target-group"
  port     = 80
  protocol = "HTTP"
  vpc_id   = aws_vpc.example_vpc.id

  health_check {
    path                = "/"
    port                = "80"
    protocol            = "HTTP"
    timeout             = 5
    interval            = 30
    healthy_threshold   = 2
    unhealthy_threshold = 2
  }
}

resource "aws_lb_listener" "example_listener" {
  load_balancer_arn = aws_lb.example_alb.arn
  port              = 80
  protocol          = "HTTP"

  default_action {
    type             = "fixed-response"
    fixed_response {
      content_type = "text/plain"
      status_code  = "200"
      content      = "OK"
    }
  }
}
