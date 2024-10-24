with open("daya.txt", "r") as f:
    text = f.read().lower()

string = "PYTHON"

if string.lower() in text:
    print("Yes Python is in the log")
else:
    print("Sorry Python is not there")