# Input: List of n elements
n = int(input("Enter the number of elements in the list: "))
elements = []

# Taking input for the list
for i in range(n):
    element = float(input(f"Enter element {i+1}: "))
    elements.append(element)

# Calculate the average
if n > 0:
    average = sum(elements) / n
    print(f"The average of the list elements is: {average}")
else:
    print("The list is empty. Cannot calculate the average.")