# terraform/main.tf

resource "aws_security_group" "fastapi_sg" {
  name        = "fastapi_sg"
  description = "Allow SSH and app port"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = var.app_port
    to_port     = var.app_port
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "fastapi_ec2" {
  ami           = "ami-0c94855ba95c71c99"  # Ubuntu 20.04 LTS in us-east-1
  instance_type = var.instance_type
  key_name      = var.key_name
  security_groups = [aws_security_group.fastapi_sg.name]

  user_data = <<-EOF
              #!/bin/bash
              apt update -y
              apt install -y docker.io docker-compose
              systemctl start docker
              systemctl enable docker

              git clone https://github.com/YOUR_USERNAME/devops-job-tracker.git
              cd devops-job-tracker
              docker-compose up --build -d
              EOF

  tags = {
    Name = "fastapi-devops-tracker"
  }
}
