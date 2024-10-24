class Employee:
    school = "KV AFS BEGUMPET" # class attributes
    def __init__ (self, name,  marks):
        self.marks = marks
        self.name = name

    def marksprint(self):
        print(f"the marks of '{self.name}' are {self.marks} in {self.school}")

    @staticmethod
    def greetings():
        print("Good day to all")


uma = Employee("Umakanth", 25)
uma.marksprint()
uma.greetings()

priya = Employee("priyanka", 98)
priya.marksprint()
priya.greetings()