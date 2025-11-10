class Employee:
    name = "divyansh"

    @classmethod
    def show (cls):
        print (f"the class atrribute of a is {cls.name}")

e = Employee()
e.name = ("harshita")

e.show()