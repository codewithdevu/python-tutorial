
# f.readlines make a list of file !

f = open("file.txt")

# read all lines in file ("file.txt")
lines = f.readlines()
print(lines, type(lines))
f.close()

# single readkines
line1 = f.readline()
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))

line4 = f.readline()
print(line4, type(line4))
f.close() 

# using while loop 
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()

