# Replacing double spaces with single spaces

name = "umakanth  is  a  good  person"

print(name)
print(name.find("  "))

print(name.replace("  ", " "))

x = (name.replace("  ", " "))

print(x.find("  ")) # if value is not found it returns (-1)
print(x)