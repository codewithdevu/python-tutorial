try:
    A = int(input("Enter A: "))
    B = int(input("Enter B: "))
    print(A/B)
except ZeroDivisionError as z:
    print("Infinite")
