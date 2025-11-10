class Employee:
    language = "python" # this  is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"the language is: {self.language} \n the salary is: {self.salary}")

    @staticmethod
    def greet(): # this method not use (self)
        print("\tDivyansh yadav")

harry = Employee()
harry.language = "javascript" # this is an instance attribute
# harry.getInfo()
harry.greet()
Employee.getInfo(harry)
