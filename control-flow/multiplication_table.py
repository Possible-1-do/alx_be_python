number = int(input("Enter a number to see its multiplication table:"))

print("\n Multiplication Table for ",number)

for i in range(1,10):
    product = number * i
    print(f"{number} * {i} = {product}")