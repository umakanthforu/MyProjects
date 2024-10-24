# ## to check for prime number


# num = int(input("Enter the number to check its prime :"))

# for x in range (2, num):
#     if((num%x)==0):
#         print("The number is not prime")
#         break
# else:
#     print("The entered number is prime")


# num = 9

# for x in range(2, num):
#     if((num%x)==0):
#             print("The number is not prime")
#             break
# else:
#     print("The number is prime")

num = 5

for i in range(2, num):
    if(num%i==0):
        print("The given number is not Prime")
        break
else:
    print("The given number is prime")