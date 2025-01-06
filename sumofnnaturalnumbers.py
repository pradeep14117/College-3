# Function to calculate the sum of n natural numbers
def sum_natural_numbers(n):
    return n * (n + 1) // 2

# Main program
n = int(input("Enter a positive integer: "))  # Take user input
if n > 0:
    result = sum_natural_numbers(n)  # Call the function
    print(f"The sum of the first {n} natural numbers is: {result}")
else:
    print("Please enter a positive integer.")
