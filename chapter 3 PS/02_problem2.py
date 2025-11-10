letter = '''Dear <|Name|>,
     You are selected !
<|Date|>'''


Name = input("enter your name : ")
date = input("enter your date: ")

print(letter.replace(f"<|Name|>", Name) .replace (f"<|Date|>", date))