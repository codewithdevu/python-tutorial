from functools import reduce

# Map example
l = [1,2,3,4,5]

square = lambda x: x*x

sqlist = map(square , l)
print(list(sqlist)) #output:  [1,4,9,16,25]

# filter example 
def even(n):
    if (n%2 == 0):
        return True
    return False

onlyEven = filter(even , l)
print(list(onlyEven)) #output: [2,4]

# Reduce Example
def sum (a,b):
    return a+b

print(reduce(sum , l)) #output:  1+2+3+4+5 = 15