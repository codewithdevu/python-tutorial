f = open("poem.txt")
content = f.read()

if ("Twinkle" in content):
    print("Twinkle word is present in the content")
else:
    print("Twinkle word is not present in the content")

f.close()