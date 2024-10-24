# class world: # defining class
#     name = "india" # class attribute
#     continent = "asia" # class attribute
#     pincode = 524004 # class attribute

#     def code(self):
#         print(f"PINCODE OF THE LOCATION IS {self.pincode}")

# umakanth = world()
# priyanka = world() # creating instance
# priyanka.name = "Anaconda" # setting Instance attribute of instance priyanka
# priyanka.pincode = 523002
# print(umakanth.name)
# print(priyanka.name)
# print(umakanth.continent)
# umakanth.code()
# priyanka.code()

# class hyderabad:
#     name = "begumpet" # Class attribute
#     place = "Balanagar"

#     def area(self):
#         print("hello world", self.place)
    
# umakanth = hyderabad()
# print(umakanth.name)
# umakanth.area()

# shanmukhi = hyderabad()
# print(shanmukhi.name)
# shanmukhi.name = "Shanmukhi" # Instance attribute
# print(shanmukhi.name)

# hyderabad.name = "Vizag" # setting class attribute
# print(umakanth.name)


class Navy:
    department = "Operations" # class attributes
    trade = "Radio"
    place = "vizag"

    def location(self):
        print("Your location is ", self.place)

    @staticmethod # static methods
    def greeting():
        print("Good Day Boss")

umakanth = Navy()
print(umakanth.department)
print(umakanth.trade)
umakanth.location() # its shortcut to call method
Navy.location(umakanth) # its the exact way to call method
umakanth.greeting()

priyanka = Navy()
priyanka.department = "Administration"
priyanka.trade = "Airframe Fitter"
priyanka.place = "New Delhi"

print(priyanka.department)
print(priyanka.trade)
priyanka.location()
priyanka.greeting()

Navy.department = "Maintenance"
Navy.trade = "ADSO"
Navy.place = "Cochin"

umakanth = Navy()
print(umakanth.department)
print(umakanth.trade)
umakanth.location()
priyanka.greeting()