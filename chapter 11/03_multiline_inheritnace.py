class Employee():
    name = "devu"
    

class programmer(Employee):
    company = "ITC INFOTECH"
   

class manager(programmer):
    language = "pyhton"
  

o = manager()

print(o.name , o.company , o.language)