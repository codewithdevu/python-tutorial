marks = {
    "Divyansh" : 100 ,
    "shubham" : 56,
    "khuswant" : 45
    }

print(marks.items()) 
print(marks.keys())
marks.update({"Heamnt" : 70}) 
print(marks)

print(marks.get("Divyansh")) #print None
print(marks["Divyansh"]) #returns an error

marks.clear()
print(marks)  # Output: {}


marks.copy()
print(marks)

