num = 1
for i in range(3):
    for j in range(2*i+1):
        print(num, end=" ")
        num += 1
    print()

#     Let's dry run this Python code step-by-step to understand how the output is generated.

# 🔁 Code:
# python
# Copy
# Edit
# num = 1
# for i in range(3):
#     for j in range(2*i + 1):
#         print(num, end=" ")
#         num += 1
#     print()
# 🧠 Understanding the loops:
# Outer loop: for i in range(3) → i will take values 0, 1, 2

# Inner loop: for j in range(2*i + 1) → controls how many numbers get printed in each row

# num starts at 1 and increases every time it's printed.

# 🔍 Dry Run:
# Iteration 1 (i = 0):
# 2*i + 1 = 2*0 + 1 = 1

# Inner loop runs 1 time (j=0)

# Prints: 1 → num becomes 2

# Output so far:

# Copy
# Edit
# 1
# Iteration 2 (i = 1):
# 2*i + 1 = 2*1 + 1 = 3

# Inner loop runs 3 times (j=0 to 2)

# Prints: 2 3 4 → num becomes 5

# Output so far:

# Copy
# Edit
# 1
# 2 3 4
# Iteration 3 (i = 2):
# 2*i + 1 = 2*2 + 1 = 5

# Inner loop runs 5 times (j=0 to 4)

# Prints: 5 6 7 8 9 → num becomes 10

# Final output:

# Copy
# Edit
# 1
# 2 3 4
# 5 6 7 8 9
# ✅ Final Output:
# Copy
# Edit
# 1
# 2 3 4
# 5 6 7 8 9
# Let me know if you'd like to reverse it, center it like a pyramid, or try a similar pattern with characters!