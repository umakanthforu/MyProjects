## DEFINING VARIABLES ##

variable "os" {
    type = string
    default = "ami-04a37924ffe27da53"
    description = "This is my Amazon AMI ID"
}

variable "instance_type" {
    type = string
    default = "t2.micro"
    description = "Best Instance for free usage"
    sensitive = false  
}

variable "name_tag" {
    type = string
    default = "MyEC2Instance"  
}

## Defining empty variable and accepting value during "Terraform Apply" command
# variable "bucket_name" {
  
# }

## declaring empty variable and accepting value using --   terraform plan -var-file="filename.tfvars"

# variable "username"{

# }
