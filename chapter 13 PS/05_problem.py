from functools import reduce
l = [4, 50, 15, 4545, 974495 , 25]

def greatest(a,b):
    if (a>b):
        return a
    return b
 
print (reduce(greatest , l )) 