provider "aws" {
  region = var.region
}

resource "aws_instance" "test_ec2" {
  count         = 3
  ami           = var.ami_id
  instance_type = "t3.micro"

  tags = merge(
    {
      Name = "TestInstance-${count.index + 1}-${var.env}"
      Environment = var.env
    },
    count.index == 2 ? {} : { Project = count.index == 0 ? "alpha" : "beta" }
  )
}

