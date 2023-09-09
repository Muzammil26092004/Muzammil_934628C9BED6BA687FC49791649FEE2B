def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Get input from the user
user_input = input("Enter a non-negative integer: ")

try:
    # Convert the user input to an integer
    n = int(user_input)

    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        result = factorial(n)
        print(f"The factorial of {n} is {result}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
