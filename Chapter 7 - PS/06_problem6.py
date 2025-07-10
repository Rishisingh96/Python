# 5! = 1 X 2 X 3 X 4 X 5

# n = int(input("Enter the number: "))
# product = 1
# for i in range(1, n+1):
#     product = product * i

# print(f"The factorial of {n} is {product}")


'''
❓ Question: “i to diya hi nahi” — Bhai i actually loop ke andar automatically assign hota hai using for i in range(...). Tumhe manually i = 1 jaise set nahi karna padta. Python for loop khud handle karta hai.
🔍 Dry Run Example (n = 5 ke liye):
Let's simulate this line by line for n = 5:

Step 1: Input
makefile
Copy
Edit
Enter the number: 5
n = 5
product = 1
Step 2: Loop Execution
for i in range(1, n+1) → range(1, 6) = [1, 2, 3, 4, 5]

i (from range)	product (before)	product = product * i	product (after)
1	1	1 × 1 = 1	1
2	1	1 × 2 = 2	2
3	2	2 × 3 = 6	6
4	6	6 × 4 = 24	24
5	24	24 × 5 = 120	120

✅ Final Output:
csharp
Copy
Edit
The factorial of 5 is 120
🔄 Loop Explanation:
Python mein for i in range(1, n+1): ka matlab hai:

Start i from 1

Go till n (inclusive)

Har step pe i ka value change hota hai automatically

Tumne i manually define nahi kiya, because for loop ne wo kaam khud kar diya.
'''

n = int(input("Enter your number: "))
fact = 1

for i in range(n, 0, -1):  # i goes from n to 1
    fact *= i

print("Factorial of", n, "is:", fact)


'''ava for (int i = n; i >= 1; i--)
This counts down from n to 1, multiplying all numbers.

Python for i in range(n, 0, -1)
This also counts from n to 1, because range(start, stop, step):

start = n

stop = 0 (but not included)

step = -1 (go in reverse)
'''