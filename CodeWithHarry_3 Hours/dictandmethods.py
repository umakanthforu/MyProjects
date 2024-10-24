dict = {"amit" : "Superman boss", "karthika" : "Awesome girl", "Shanmukhi" : "All rounder man"} # to define as dictionary
# print (dict, type(dict))

# set1 = set() # to define as empty set
# print (set1, type(set1)) 
print (dict)
dict["umakanth"] = 99
print (dict)
dict["priyanka"] = 100
print (dict)
print(dict["umakanth"])  # to print marks of umakanth
print(dict.get("karthiika")) # to avoid throwing error if name is not available
# print(dict.get["karthika"])
print(dict.keys()) # to print keys of dictionary
print (dict.values()) # to print values of dictionary