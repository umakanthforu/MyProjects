m1 = int(input("Enter the marks of first student : \t"))
m2 = int(input("Enter the marks of second student : \t"))
m3 = int(input("Enter the marks of third student : \t"))
m4 = int(input("Enter the marks of fourth student : \t"))
m5 = int(input("Enter the marks of fifth student : \t"))
m6 = int(input("Enter the marks of sixth student : \t"))

mylist = [m1, m2, m3, m4, m5, m6]
mylist.sort()
mylist.reverse()
print ("The list of marks you entered is : \n", mylist)