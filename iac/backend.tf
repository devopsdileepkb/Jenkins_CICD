terraform {
  backend "s3" {
    bucket       = "jenkins-cicd-terraform-state-894208478712"   # unique bucket name
    key          = "eks/terraform.tfstate"
    region       = "us-west-2"
    encrypt      = true
    use_lockfile = true   # replaces dynamodb_table
  }
}
