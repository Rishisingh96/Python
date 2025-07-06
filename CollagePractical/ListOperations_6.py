# Program to demonstrate list operations in Python

# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Original List:", fruits)

# Append an item
fruits.append("orange")
print("After append:", fruits)

# Insert at a specific position
fruits.insert(1, "mango")
print("After insert at index 1:", fruits)

# Remove an item
fruits.remove("banana")
print("After removing 'banana':", fruits)

# Sort the list
fruits.sort()
print("After sorting:", fruits)

# Copy the list
fruits_copy = fruits.copy()
print("Copied List:", fruits_copy)

# Find index of an element and replace it
index = fruits.index("apple")
fruits[index] = "kiwi"
print("After replacing 'apple' with 'kiwi':", fruits)
