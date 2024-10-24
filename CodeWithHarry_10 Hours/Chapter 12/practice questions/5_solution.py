try:
    a = int(input("Enter the first number"))
    b = int(input("Enter the second number"))
    print(a/b)
except ZeroDivisionError as e:
    print("Error occured as Infinity Error")
print("Execution done")