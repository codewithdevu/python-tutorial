def greatest(a,b,c):
    if (a>b and a>c):
        return a 
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
a = int(input("Enter your number: "))   
b = int(input("Enter your number: "))   
c = int(input("Enter your number: "))  

print( "the greatest number is:",greatest(a,b,c))