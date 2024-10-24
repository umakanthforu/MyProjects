# Q letter template for name replacement

data1 = input("Enter your name :")
data2 = input("Enter your place :")

template = '''
Hi \"<name>\" \n You are posted to \t \'<place>\''''

print(template.replace("<name>", data1).replace("<place>", data2))
