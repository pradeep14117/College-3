# Data
data = [
    {"name": "John", "gender": "boy", "age": 20},
    {"name": "Alice", "gender": "girl", "age": 17},
    {"name": "Tom", "gender": "boy", "age": 19},
    {"name": "Lucy", "gender": "girl", "age": 21},
    {"name": "Emma", "gender": "girl", "age": 15},
]

# Initialize counts
boys_count = 0
girls_count = 0
boys_above_18 = 0
girls_above_18 = 0

# Process data
for person in data:
    if person["gender"] == "boy":
        boys_count += 1
        if person["age"] > 18:
            boys_above_18 += 1
    elif person["gender"] == "girl":
        girls_count += 1
        if person["age"] > 18:
            girls_above_18 += 1

# Output results
print(f"Total Boys: {boys_count}")
print(f"Total Girls: {girls_count}")
print(f"Boys above 18: {boys_above_18}")
print(f"Girls above 18: {girls_above_18}")