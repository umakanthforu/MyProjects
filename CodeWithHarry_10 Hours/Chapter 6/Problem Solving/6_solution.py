### calculate the grade based on marks

marks = int(input("Enter the marks obtained :"))

if (marks>=90 and marks<=100):
    print(" Its Excellent", marks)
elif (marks>=80 and marks<=89):
    print("Its A", marks)
elif (marks>=70 and marks<=79):
    print("Its B", marks)
elif (marks>=60 and marks<=69):
    print("Its C", marks)
elif (marks>=50 and marks<=59):
    print("Its D", marks)
else:
    print("Its E", marks)