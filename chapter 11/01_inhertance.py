class Employee: # base class
    company = "ITC"
    def show (self):
        print(f"the name of the Employee is {self.name} and the company is {self.company}")

# class programmer:
#     company = "ITC INFOTECH"
#     def show(self):
#         print(f"the name is {self.name} and the company is {self.company}")

class programmer(Employee): # deriver or child class 
    company = "ITC INFOTECH"
    def showlanguage(self):
        print(f"the name is {self.name} and he is good with {self.language} language")

a = Employee()
b = programmer()

print(a.company , b.company)
