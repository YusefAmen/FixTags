variable "region" {
  description = "AWS region"
  type = string
  default = "us-west-1"
}

variable "ami_id" {
  description = "Amazon Linux 2 AMI"
  default     = "ami-020fbc00dbecba358"
}

variable "env" {
  description = "Environment name"
  type = string
}

variable "aws_secret_key" {
  description = "Secret Key AWS"
  type = string
}

variable "aws_access_key" {
  description = "Access Key AWS"
  type = string
}
