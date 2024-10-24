### program to copy of text file ##

with open("daya.txt", "r") as f:
    olddata = f.read()

with open("newfile.txt", "w") as f:
    f.write(olddata)