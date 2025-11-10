class Employee: # base class
    company = "ITC"
    name = "devu"
    def show (self):
        print(f"the name of the Employee is {self.name} and the company is: {self.company}.")

class coder: # base class
    language = "pyhton"
    def printlanguage(self):
        print(f"out of all language here is your language: {self.language}.")

class programmer(Employee,coder): # derived or child class
    company = "ITC INFOTECH"
    def showlanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language.")
 
a = programmer()

a.show()
a.printlanguage()
a.showlanguage()
