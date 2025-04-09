output "instance_ids" {
  value = [for i in aws_instance.test_ec2 : i.id]
}

output "instance_tags" {
  value = [for i in aws_instance.test_ec2 : i.tags]
}
