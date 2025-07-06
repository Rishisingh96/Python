# Program to compare areas of two rectangles

# Input for Rectangle 1
length1 = float(input("Enter length of Rectangle 1: "))
width1 = float(input("Enter width of Rectangle 1: "))
area1 = length1 * width1

# Input for Rectangle 2
length2 = float(input("Enter length of Rectangle 2: "))
width2 = float(input("Enter width of Rectangle 2: "))
area2 = length2 * width2

# Displaying comparison result
if area1 > area2:
    print("Rectangle 1 has a greater area.")
elif area2 > area1:
    print("Rectangle 2 has a greater area.")
else:
    print("Both rectangles have equal area.")
