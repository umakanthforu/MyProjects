dict = {}

for i in range(4):
    key = input("Enter your name :")
    if (dict.get(key))==None:
        value = input("Enter your language :")
        dict.update({key : value})
    else:
        print("The name is already registered, please try again")

# print(dict)
for a, b in dict.items():
    print("The name you entered is ",a, "The language you prefered is ", b)