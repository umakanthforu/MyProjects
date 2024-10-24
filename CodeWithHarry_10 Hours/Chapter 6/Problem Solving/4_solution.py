# to check the length of username is less than 10
mylist = []

for uname in range(3):
    uname = input("Enter the username :")
    x = len(uname)
    if (x<10):
          print("Please enter the username with more than 10 charecters :")
    else:
          mylist.append(uname)
          print(mylist)
