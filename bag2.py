# Example dictionary
data = {"boy": 18, "girl": 11, "boy2": 20, "girl2": 25, "boy3": 15, "girl3": 19}

# Initialize counters
total_boys = 0
total_girls = 0
boys_above_18 = 0
girls_above_18 = 0

# Iterate through the dictionary
for key, age in data.items():
    if "boy" in key.lower():
        total_boys += 1
        if age > 18:
            boys_above_18 += 1
    elif "girl" in key.lower():
        total_girls += 1
        if age > 18:
            girls_above_18 += 1

# Display results
print(f"Total number of boys: {total_boys}")
print(f"Total number of girls: {total_girls}")
print(f"Number of boys above 18: {boys_above_18}")
print(f"Number of girls above 18: {girls_above_18}")