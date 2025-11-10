# 5! = 1 х 2 х 3 х 4 х 5 

n = int (input("Enter the number: "))
product = 1 
for i in range (1, n+1):
    product = product*i

print(f"The factorial of {n} is {product}")