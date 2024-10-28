# ## LEARNING HASHICORP CONFIGURATION LANGUAGE ##


# #  1. Blocks in HCL

# # BLOCK TYPES : Provider, Resource, Variable, Data and Output Blocks

# block_type {
#     attribute1 = value1
#     attribute2 = value2
# }

# -------------------------------------------------------------------------
# # 2.  Attributes are "Key and Value Pairs"
# key = value1

# -------------------------------------------------------------------------
# # 3.  Datatypes

# - Strings
# - Numbers
# - Boolean Values
# - List
# example : mylist = ["sg-123454", "sg-98765"]

# - Maps
# syntax:
# variable "mymap" {
#     type = map
#     default = { key1 = "Value1", key2 = "Value2"}
# }

# Example:

# locals {
#     my_map = {"name" = "John Doe", "age" = 34, "is_admin" = true}
# }

# locals.my_map["age"]

# -------------------------------------------------------------------------
# # 4.   Conditions

# ## condition : IF variable "var.instance" is development, use t2.micro or else use t2.small

# resource "aws_instance" "server"{
#     instance_type = var.instance == "development" ? "t2.micro" : "t2.small"
# }

# -------------------------------------------------------------------------
# # 5.   Function

# myfunction {
#     name = "John Cena"
#     fruits = ["apple", "banana", "grapes"]
#     message = "Hello. ${upper(myfunction.name)} ! I know you like ${join(",", myfunction.fruits)}"
# }

# OUTPUT : Hello JOHN CENA! I know you like apple, banana, grapes.

# -------------------------------------------------------------------------
# # 6.   Resource Dependency

# # WE CAN CALL second resource id from first resource.

# resource "aws_instance" "myserver"{
#     vpc_security_group_ids = aws_security_group.mysg.id
# }

# resource "aws_security_group" "mysg"{
#     # inbound rules
# }


 