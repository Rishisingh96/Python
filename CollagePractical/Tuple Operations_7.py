# Program to demonstrate use of tuples

# Creating a tuple
colors = ("red", "green", "blue", "yellow")
print("Original Tuple:", colors)

# Access elements
print("First color:", colors[0])
print("Last color:", colors[-1])

# Slicing a tuple
print("Slice (1 to 3):", colors[1:3])

# Tuple length
print("Length of tuple:", len(colors))

# Loop through tuple
print("Loop through tuple:")
for color in colors:
    print(color)

# Tuple is immutable, can't change items
# colors[0] = "purple" → ❌ Will throw error
