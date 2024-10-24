# mydict = {"name" : "Umakanth Achukolu" , "Service No.": 794032, "rank" : "Sergeant", "trade": "Radio Technician", "mylist" : [23, 45, 67], "mytuple" : (23, 45, "auk")}


# print(mydict)
# print(mydict["name"])

# print(mydict.items()) # prints all elements
 
# for a, b in mydict.items(): # it returns the list of keys and values
#     print(a,"=", b)

# for key in mydict.keys(): # it returns just the keys
#     print(key)

# mydict.update({"harry" : "He is a trainer", "mylist" : "1, 2 ,3"})

# for key, value in mydict.items():
#     print(key, "=", value)


# TO PRINT ALL ITEMS AND KEYS

# print(mydict.items())

# for a, b in mydict.items():
#     print (a, b)

# for key in mydict.keys():
#     print(key)

#### TO UPDATE DICTIONARY #####

mydict = {"name" : "Umakanth Achukolu" , "Service No.": 794032, "rank" : "Sergeant", "trade": "Radio Technician", "mylist" : [23, 45, 67], "mytuple" : (23, 45, "auk")}

# mydict.update({"name" : "Priyanka", "Daughter" : "Karthika", "mylist" : "[1, 2 ,3]"})  # to update dictionary

# for key, value in mydict.items(): # to print all items
#     print(key, value)

# for a in mydict.keys(): # to print all keys
#     print(a)

# for b in mydict.values(): # to print all values
#     print(b)

print(mydict.get("name")) # it gives output of key name
print(mydict.get("serial")) # it give output none as serial is not there is dictioinary