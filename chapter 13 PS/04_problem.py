def division5(n):
    if(n%5==0):
        return True
    return False

a = [4, 50, 15, 4545, 974495 , 25]

f = list(filter(division5 , a))
print(f)