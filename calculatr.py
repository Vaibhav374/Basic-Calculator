# Define a function for addition
def add(x, y):
    return x + y

# Define a function for subtraction
def subtract(x, y):
    return x - y

# Define a function for multiplication
def multiply(x, y):
    return x * y

# Define a function for division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero is not allowed."

# Print the welcome message and available operations
print("===== BASIC PYTHON CALCULATOR =====")
print("Choose an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Loop to keep the calculator running until user exits
while True:
    # Take user input for choice
    choice = input("Enter your choice (1/2/3/4): ")

    # Check if the choice is valid
    if choice in ['1', '2', '3', '4']:
        try:
            # Take input for two numbers and convert to float
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print(" Invalid input! Please enter valid numbers.")
            continue

        # Perform the selected operation
        if choice == '1':
            print(f" Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f" Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f" Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")

        # Ask user whether to perform another calculation
        next_calc = input(" Do you want to perform another calculation? (yes/no): ").lower()
        if next_calc != 'yes':
            print(" Thank you for using the calculator. Goodbye!")
            break
    else:
        print(" Invalid choice! Please choose from 1, 2, 3, or 4.")
