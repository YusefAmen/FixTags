#!/bin/bash
ENV=$1

if [ -z "$ENV" ]; then
  echo "❌ Usage: ./apply.sh [dev|staging|prod]"
  exit 1
fi

echo "Using AWS profile: $ENV"
export AWS_PROFILE=$ENV

terraform init -backend-config="${ENV}-backend.tfvars" || terraform init
terraform apply -var-file="$1.tfvars"
