class Employee:
    language = "python" # this  is a class attribute
    salary = 1200000

harry = Employee()
harry.name = "harry" # this is an object attribute
print (harry.name , harry.language, harry.salary)

divyansh = Employee()
divyansh.name = "divyansh" # this is an object attribute
print (divyansh.name , divyansh.language, divyansh.salary)

# here name is object attribute and salary and language are class attributes as they directry belong to the classs 