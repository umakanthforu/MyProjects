dict = {
    "kursey" : "chair",
    "Ghadi" : "clock",
    "diwar" : "wall" 
}


# for a, b in dict.items():
#     print(a, b)

name = input("Enter the hindi word to check the english meaning :")

if ((dict.get(name))==None):
    print("Word not foudn please try again")
else:
    print("The english meaning of word is :", (dict.get(name)))













