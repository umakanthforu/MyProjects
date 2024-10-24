try:
    with open("1.txt", "r") as f:
        f.read()
    with open("2.txt", "r") as f:
        f.read()
    with open("3.txt", "r") as f:
        f.read()
except Exception as error:
    print("Below mentioned error has occured")
    print(error)