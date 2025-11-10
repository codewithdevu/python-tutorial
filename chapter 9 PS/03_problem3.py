
# Function to generate a multiplication table for a number n
def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i} = {n * i}\n"

# Write the table to a text file in the 'tables' folder
    with open(f"tables/table_{n}.txt", "w") as f:
        f.write(table)

# Generate tables for numbers 2 to 20
for i in range(2, 21):
    generateTable(i)

