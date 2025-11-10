class demo:
    a = 4

o = demo()
print(o.a) # print the class attribute because instance attribute is not present

o.a = 0 #instance attribute is set

print(o.a) # prints the instance attribute because instance attribute is present

print(demo().a) # print the class attribute 