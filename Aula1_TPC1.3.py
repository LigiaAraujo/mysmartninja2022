#exercise 1.3 - Calculator

num1 = int(input("Type a number: "))
num2 = int(input("Type a number: "))

operation = input("Choose your operation: ")

if operation == "+":
    print(num1 + num2)
elif operation == "-":
    print(num1 - num2)
elif operation == "*":
    print(num1 * num2)
elif operation == "/":
    print(num1 / num2)
else:
    print("Select another operation: ")