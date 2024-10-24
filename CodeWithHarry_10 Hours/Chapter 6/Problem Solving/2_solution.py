# three subjects marks average shoud be above 40 and individual marks should be above 33

sub1 = int(input("Enter your marks in first subject :"))
sub2 = int(input("Enter your marks in second subject :"))
sub3 = int(input("Enter your marks in third subject :"))
average = (sub1 + sub2 + sub3)/3

if (average >= 40):
    if (sub1 >=33 and sub2 >= 33 and sub3 >=33):
        print("Congratulations you have passed the exam.")
    else:
        print("You have failed the exam due to subject failure")
else:
    print("You have failed the exam due to average below 40 Percentage")