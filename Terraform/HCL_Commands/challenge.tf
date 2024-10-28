# CHALLENGE : creat a file in local machine using terraform

resource "null_resource" "name" {
    provisioner "local-exec" {
        command = "echo 'Message: ${upper("Hello World")}' > challenge.txt"
        }
    }