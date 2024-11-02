class ongole:
    def __init__(self, number):
        self.number = number
    
    def mulitple(self):
        print(f"The multiple of {self.number} is {self.number/2}")

a = int(input("Enter the number :"))

newvalue = ongole(a)
newvalue.mulitple()