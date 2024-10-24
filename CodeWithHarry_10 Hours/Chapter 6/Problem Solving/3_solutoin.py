### FOR SPAM CHECK IN MAIL CONTENT


spamwords = ["buy now", "subscribe now", "play now"]

email = input("Enter the mail content to check for spam :").lower()
spam = False

if ("buy now" in email):
    spam = True

elif("subscribe now" in email):
    spam = True

elif("play now" in email):
    spam = True

else:
    spam = False

print("The email content of spam is ", spam)
