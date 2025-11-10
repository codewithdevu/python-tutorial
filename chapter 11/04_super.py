class Employee():
    def __init__(self):
        print("constructor of Employee")
    name = "devu"
    

class programmer(Employee):
    def __init__(self):
        print("constructor of programmer")
    company = "ITC INFOTECH"
   

class manager(programmer):
    def __init__(self):
        super().__init__()
    print("constructor of manager")
    language = "pyhton"
  

o = manager()

print(o.name , o.company , o.language)