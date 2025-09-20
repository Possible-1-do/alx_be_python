number = int(input(f"Enter a number to see its multiplication table:"))

print("\n Multiplication Table for ",number)

for i in range(1,10):
    print(number, "x", i ,"=" , number*i)