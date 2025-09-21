
# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Row counter for while loop
row = 0

# While loop to go through each row
while row < size:
    
    for col in range(size):
        print("*", end="")
    print()  # Move to the next line after finishing a row
    row += 1
