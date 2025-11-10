for i in range (10):
    if(i==6):
        break #Exit the loop right now 
    print(i)


for i in range(15):
    if(i==9):
        continue #skip this iteration
    print(i)

for i in range (100):
    if i in [10,20,30,40,50]:
        continue
    print(i)