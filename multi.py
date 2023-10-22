def calculator():
    print("Calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter an operation (+, -, *, /): ")

    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 == 0:
            result = "Cannot divide by zero"
        else:
            result = num1 / num2
    else:
        result = "Invalid operation"

    print("Result:", result)

def palindrome_checker():
    print("Palindrome Checker")
    word = input("Enter a word: ").lower()
    if word == word[::-1]:
        print("It's a palindrome!")
    else:
        print("It's not a palindrome.")

while True:
    print("MENU:")
    print("1. Calculator")
    print("2. Palindrome Checker")
    print("3. Quit")
    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        calculator()
    elif choice == "2":
        palindrome_checker()
    elif choice == "3":
        break
    else:
        print("Invalid choice. Please select a valid option.")
