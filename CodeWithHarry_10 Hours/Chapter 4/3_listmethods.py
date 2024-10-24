myListOfNumbers  = [25, 13, 45, 78, 1, 9, 3, 5]
print(myListOfNumbers)

print(myListOfNumbers.sort()) # it sorts list in ascending order doesnt return any value
print(myListOfNumbers)

print(myListOfNumbers.reverse()) # it reverses the original list
print(myListOfNumbers)

myListOfNumbers.append(9)  # append inserts at the end of the list
print(myListOfNumbers)

myListOfNumbers.insert(1, 12345) # it inserts number 12345 at index 1
print(myListOfNumbers)

myListOfNumbers.pop() # removes the last element in the list
myListOfNumbers.pop()
myListOfNumbers.pop()
myListOfNumbers.pop()
print(myListOfNumbers)

myListOfNumbers.append("priyanka") # adds string to the list
myListOfNumbers.insert(0, "umakanth") # adds string at the mentioned index
print(myListOfNumbers)

myListOfNumbers.remove("umakanth") # removes first occuring element from the list
print(myListOfNumbers)

myListOfNumbers.extend([25, 50, 75, 100]) # extends the list of elements with given elements in square brackets
print(myListOfNumbers)