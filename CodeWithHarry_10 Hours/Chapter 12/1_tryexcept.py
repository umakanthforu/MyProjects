try:
    num1 = int(input("Enter first number :"))
    num2 = int(input("Enter second number :"))
    
    print(f"the sum of two numbers entered is {num1 + num2}")

except Exception as e:

    print("Below mentioned error has occured")
    print(e)

print("There were no errors")   