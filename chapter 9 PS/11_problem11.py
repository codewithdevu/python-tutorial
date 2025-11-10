import os

with open("old.txt") as f:
    content = f.read()

with open("renamed_by_python.txt", "w") as f:
    f.write(content)

# Delete the old file
os.remove("old.txt")

