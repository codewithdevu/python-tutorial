mylist = [1,2,9,5,3,5]

squaredlist = []
for item in mylist:
    print(f"the square of number {item} is {item*item} ")
    squaredlist.append(item*item)

# using list comprehension method 

squaredlist = [i*i for i in mylist]

print(squaredlist)