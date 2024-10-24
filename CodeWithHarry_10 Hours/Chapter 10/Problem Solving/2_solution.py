import math
class calculator:

    def __init__ (self, num):
        self.num = num
    
    def sqrt(self):
        print(f"The square root of given number is {math.sqrt(self.num)}")
    
    def square(self):
        print(f"The sqaure of the given number is {self.num * self.num}")
    
    def cube(self):
        print(f"The cube of the given number is {self.num*self.num*self.num}")

number = calculator(3)
number.sqrt()
number.cube()
number.square()