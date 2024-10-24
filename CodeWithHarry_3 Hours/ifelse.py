age = int(input ("Enter your age:"))

if(age>=18):
    print("Congratulations boss you r an adult")
elif(age==0):
    print("you are not yet born ", age)
elif(age>=1 and age<=10):
    print("you are between 1 to 10 and your age is ", age)

elif(age>=11 and age<=15):
    print("you are between 11 and 15 and your age is", age)

else:    
    print("Chill bro your need to grow up...!", age)

print("End of the program")