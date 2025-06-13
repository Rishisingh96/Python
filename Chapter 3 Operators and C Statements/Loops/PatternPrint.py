# Pattern 1: Right-Angled Triangle (Increasing Stars)
print("\nPattern 1: Right-Angled Triangle (Increasing Stars)")
rows = 5
for i in range(1, rows + 1):
    print('*' * i)

# Pattern 2: Right-Angled Triangle (Decreasing Stars)
print("\nPattern 2: Right-Angled Triangle (Decreasing Stars)")
for i in range(rows, 0, -1):
    print('*' * i)

# Pattern 3: Right-Aligned Triangle
print("\nPattern 3: Right-Aligned Triangle")
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * i)

# Pattern 4: Pyramid (Centered)
print("\nPattern 4: Pyramid (Centered)")
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))

# Pattern 5: Inverted Pyramid
print("\nPattern 5: Inverted Pyramid")
for i in range(rows, 0, -1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))

# Pattern 6: Diamond Pattern
print("\nPattern 6: Diamond Pattern")
# Upper part
for i in range(1, rows + 1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))
# Lower part
for i in range(rows - 1, 0, -1):
    print(' ' * (rows - i) + '*' * (2 * i - 1))

# Pattern 7: Half Pyramid using Numbers
print("\nPattern 7: Half Pyramid using Numbers")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()

# Pattern 8: Floyd's Triangle
print("\nPattern 8: Floyd's Triangle")
num = 1
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(num, end=' ')
        num += 1
    print()

# Pattern 9: Binary Triangle (0 and 1 alternate)
print("\nPattern 9: Binary Triangle")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print((i + j) % 2, end='')
    print()

# Pattern 10: Pascal's Triangle
print("\nPattern 10: Pascal's Triangle")
for i in range(rows):
    num = 1
    print(' ' * (rows - i), end='')
    for j in range(i + 1):
        print(num, end=' ')
        num = num * (i - j) // (j + 1)
    print()
