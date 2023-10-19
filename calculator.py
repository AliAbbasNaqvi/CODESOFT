# 1.Add
# 2.Subtract
# 3.multiply
# 4.Divide


print("Select an operation to perform: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

operation = input()

# code for add
if operation == "1":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The sum is ", str(int(num1) + int(num2)))

# code for subtract
elif operation == "3":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The difference is ", str(int(num1) - int(num2)))

# code for divide
elif operation == "4":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The product is ", str(int(num1) * int(num2)))

# code for divide
elif operation == "4":
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    print("The dividion is ", str(int(num1) / int(num2)))

# code for invalid operation
else:
    print("invalid")
