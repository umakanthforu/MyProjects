# uma = open("uma.txt", "r")
# reader = uma.read()
# print(reader)


with open("uma.txt", "r") as uma:
    reader = uma.read()
    print(reader)