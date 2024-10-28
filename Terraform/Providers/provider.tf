## PROVIDER AWS ##

provider "aws" {
  # Configuration options
  region = "ap-south-1"
}

## PROVIDER AWS using ALIAS ##

provider "aws" {
  # Configuration options
  region = "us-east-1"
  alias = "useast"
}

## PROVIDER GITHUB ##

provider "github" {
  # Configuration options
  token = "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"
}