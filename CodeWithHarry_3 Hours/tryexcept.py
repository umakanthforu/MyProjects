# SIMPLE ERROR EXCEPTION 
# try:
#     a = int(input("Enter any number"))
#     print (a)
# except:
#     print("Some error occured")


# WITH ERROR DESCRIPTION
try:
    a = int(input("Enter any number :"))
    print (a)
except Exception as error:
    print ("Some error occured :", error)