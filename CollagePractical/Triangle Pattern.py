# Program to print a triangle pattern using asterisks

rows = int(input("Enter number of rows for the triangle: "))

# Outer loop for each row
for i in range(1, rows + 1):
    # Inner loop for spaces
    print(' ' * (rows - i), end='')
    # Inner loop for stars
    print('*' * (2 * i - 1))
