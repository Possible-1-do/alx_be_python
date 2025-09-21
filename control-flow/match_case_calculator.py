num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Choose the operation(+,-,*,/):")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = int(input("Enter your choice:"))

match choice:
    case 1:
        print("The result is",num1 + num2)
    case 2:
        print("The result is",num1 - num2)
    case 3:
        print("The result is",num1 * num2)
    case 4:
        if num2 != 0:
            print("The result is",num1 / num2)
        else:
            print("Cannot divide by zero")
    case _:
        print("You entered a wrong choice")
         