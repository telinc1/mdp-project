provider "aws" {
  region = "eu-central-1"
}

resource "aws_ecr_repository" "wwtbam" {
  name = "wwtbam-ecr"
}

output "url" {
  value = aws_ecr_repository.wwtbam.repository_url
}
