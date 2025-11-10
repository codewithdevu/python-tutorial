class programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("divyansh", 1200000, 305001)
print(p.name, p.salary, p.pin, p.company)
r = programmer("rohan", 1200000, 305001)
print(r.name, r.salary, r.pin, r.company)
        