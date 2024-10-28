

## configured AK & SAK using aws configure command ##

## CREATE AWS RESOURCE OF EC2 INSTANCE ##

resource "aws_instance" "web" {
  ami           = var.os ## fetches the value from declared variable "os"
  instance_type = var.instance_type
  provider = aws

  tags = {
    Name = var.name_tag
  }
}

# CREATE A S3 BUCKET ##

# resource "aws_s3_bucket" "mybucket" {
#     bucket = var.bucket_name
# }

## CREATE AN AWS IAM USER ###

# resource "aws_iam_user" "newuser"{
#     name = "${var.username}-user"
# }


## CREATE RESOURCE OF GITHUB REPOSITORY  ##

# resource "github_repository" "example" {
#   name        = "UmaRepoByTerraform"
#   description = "CreatedUsingTerraform"

#   visibility = "public"
# }


## OUTPUTS ##
## GIVES OUTPUT AS IP ADDRESS OF INSTANCE RUNNING ##
output "IPaddress" {
    value = aws_instance.web.public_ip  
}

output "DNS" {
    value = aws_instance.web.public_dns 
}