# Program to navigate and manipulate lists, dictionaries, and tuples

# List of dictionaries (e.g., student records)
students = [
    {"name": "Rishi", "age": 22, "grades": (85, 90, 88)},
    {"name": "Aarav", "age": 21, "grades": (78, 80, 82)},
    {"name": "Diya", "age": 23, "grades": (92, 95, 94)}
]

# Navigating through the list
for student in students:
    print(f"\nName: {student['name']}")
    print(f"Age: {student['age']}")
    
    # Accessing tuple inside dictionary
    print("Grades:", student['grades'])
    average = sum(student['grades']) / len(student['grades'])
    print("Average Grade:", round(average, 2))
    
    # Adding a new key-value pair to dictionary
    student["status"] = "Passed" if average >= 80 else "Needs Improvement"

# Final data with status
print("\nUpdated Student Records:")
for student in students:
    print(student)
