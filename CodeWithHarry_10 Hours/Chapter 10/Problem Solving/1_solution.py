## program for storing information ##

class programmer:
    def __init__ (self, name, language):
        self.name = name
        self.language = language

    def details(self):
        print(f" {self.name} is expert in {self.language}")

uk = programmer("priyanka", "Java")
uk.details()