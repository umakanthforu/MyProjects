## PROGRAM TO FIND OUT GIVEN NAME IS IN LIST OR NOT


family = ['UMAKANTH', 'PRIYANKA', 'SHANMUKHI', 'KARTHIKA']

name = input("Enter any name to check, whether he is a family member or not :").upper()

if name in family:
    print("congratulations you are the family member")
else:
    print("Sorry you are not our family member")