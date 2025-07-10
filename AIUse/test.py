✅ 1. Program to print the Fibonacci series up to n terms

# Fibonacci Series up to n terms
def print_fibonacci(n):
    a, b = 0, 1
    print("Fibonacci series:")
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

# Example usage
n = int(input("Enter number of terms: "))
print_fibonacci(n)
✅ 2. Program to check if a string is a palindrome
python
Copy
Edit
# Check Palindrome String

def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Optional: ignoring case and spaces
    return s == s[::-1]

# Example usage
text = input("Enter a string: ")
if is_palindrome(text):
    print("Palindrome")
else:
    print("Not a Palindrome")
✅ 3. Program to find the factorial of a number
python
Copy
Edit
# Factorial of a Number

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# Example usage
num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")
✅ 4. Program to reverse a number
python
Copy
Edit
# Reverse a Number

def reverse_number(n):
    rev = 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev

# Example usage
num = int(input("Enter a number: "))
print(f"Reversed Number: {reverse_number(num)}")
✅ 5. Program to count vowels in a string
python
Copy
Edit
# Count Vowels in a String

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Example usage
text = input("Enter a string: ")
print("Number of vowels:", count_vowels(text))
Shall I continue with the next 5 (from Armstrong to Palindrome number check) in the next message?

Let me know if you'd like all at once or one-by-one for copy-pasting ease.









Ask ChatGPT
You said:
next


ChatGPT said:
Great Rishi! Let's continue with the next 5 programs from your list — clean, correct Python code for each:

✅ 6. Program to check Armstrong number
An Armstrong number (for 3 digits) is a number such that
sum of its digits raised to the power 3 equals the number itself
e.g., 153 → 1³ + 5³ + 3³ = 153

python
Copy
Edit
# Check Armstrong Number

def is_armstrong(num):
    digits = str(num)
    power = len(digits)
    return num == sum(int(d)**power for d in digits)

# Example usage
n = int(input("Enter a number: "))
if is_armstrong(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
✅ 7. Program to check Prime number
python
Copy
Edit
# Check Prime Number

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
num = int(input("Enter a number: "))
if is_prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")
✅ 8. Program to print all prime numbers in a given range
python
Copy
Edit
# Print all Prime Numbers in a Given Range

def print_primes(start, end):
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=' ')

# Reusing is_prime() from above
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage
s = int(input("Enter start of range: "))
e = int(input("Enter end of range: "))
print_primes(s, e)
✅ 9. Program to check Perfect number
A Perfect number is a number that is equal to the sum of its proper divisors (excluding itself).
Example: 28 → 1 + 2 + 4 + 7 + 14 = 28

python
Copy
Edit
# Check Perfect Number

def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

# Example usage
num = int(input("Enter a number: "))
if is_perfect(num):
    print("Perfect Number")
else:
    print("Not a Perfect Number")
✅ 10. Program to print the sum of digits of a number
python
Copy
Edit
# Sum of Digits of a Number

def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

# Example usage
num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))
Let me know when you're ready — I’ll continue with the final 6:

➡️ Palindrome number, GCD, Swap without third variable, Remove punctuation, Character classification, Sort without sort()
And also Anagram check.

Ready for the next batch?








You said:
next


ChatGPT said:
Perfect Rishi! Here’s the final batch of your list — 6 clean and correct Python programs:

✅ 11. Program to check if a number is palindrome
A number is a palindrome if it reads the same forward and backward.

python
Copy
Edit
# Check if Number is Palindrome

def is_number_palindrome(n):
    return str(n) == str(n)[::-1]

# Example usage
num = int(input("Enter a number: "))
if is_number_palindrome(num):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
✅ 12. Program to find GCD of two numbers
GCD (Greatest Common Divisor) is the largest number that divides both numbers.

python
Copy
Edit
# Find GCD of Two Numbers

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(f"GCD of {x} and {y} is {find_gcd(x, y)}")
✅ 13. Program to swap two numbers without using a third variable
python
Copy
Edit
# Swap Two Numbers Without Using Third Variable

def swap_numbers(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

# Example usage
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
x, y = swap_numbers(x, y)
print(f"After swapping: x = {x}, y = {y}")
✅ 14. Program to remove all punctuation from a string
python
Copy
Edit
# Remove All Punctuation from a String

import string

def remove_punctuation(s):
    return ''.join(c for c in s if c not in string.punctuation)

# Example usage
text = input("Enter a string: ")
print("Without punctuation:", remove_punctuation(text))
✅ 15. Program to count digits, alphabets, spaces, and symbols in string
python
Copy
Edit
# Count Digits, Alphabets, Spaces, Symbols

def count_characters(s):
    digits = alphabets = spaces = symbols = 0
    for char in s:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            alphabets += 1
        elif char.isspace():
            spaces += 1
        else:
            symbols += 1
    return digits, alphabets, spaces, symbols

# Example usage
text = input("Enter a string: ")
d, a, sp, sym = count_characters(text)
print(f"Digits: {d}, Alphabets: {a}, Spaces: {sp}, Symbols: {sym}")
✅ 16. Program to sort a list without using sort()
python
Copy
Edit
# Sort a List Without Using sort()

def manual_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

# Example usage
nums = list(map(int, input("Enter numbers separated by space: ").split()))
sorted_list = manual_sort(nums)
print("Sorted List:", sorted_list)
✅ 17. Program to check if two strings are anagrams
Anagrams: same characters in different order (case insensitive, spaces ignored)

python
Copy
Edit
# Check Anagram Strings

def are_anagrams(str1, str2):
    s1 = sorted(str1.replace(" ", "").lower())
    s2 = sorted(str2.replace(" ", "").lower())
    return s1 == s2

# Example usage
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if are_anagrams(str1, str2):
    print("Anagram Strings")
else:
    print("Not Anagram Strings")
✅ Done! You now have a complete, clean, and ready-to-run collection of Python programs for common logic questions — perfect for viva, practicals, interviews, and practice.

Would you like a single .txt or .py file with all of these combined together as well?








You said:
write some more most importent question with solution form my semester Practical Exam  ,like reverse string , and more 


ChatGPT said:
Absolutely Rishi! Here's a handpicked list of most important Python logic-based practical questions — commonly asked in semester practical exams, viva rounds, and basic interview rounds. Each comes with a clean and correct solution:

✅ 1. Reverse a String
python
Copy
Edit
# Reverse a String

def reverse_string(s):
    return s[::-1]

# Example usage
text = input("Enter a string: ")
print("Reversed String:", reverse_string(text))
✅ 2. Check if a Number is Even or Odd
python
Copy
Edit
# Check Even or Odd

def is_even(n):
    return n % 2 == 0

# Example usage
num = int(input("Enter a number: "))
print("Even" if is_even(num) else "Odd")
✅ 3. Find Maximum and Minimum in a List
python
Copy
Edit
# Find Max and Min in a List

def find_max_min(lst):
    maximum = minimum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
    return maximum, minimum

# Example usage
nums = list(map(int, input("Enter numbers: ").split()))
max_val, min_val = find_max_min(nums)
print("Maximum:", max_val)
print("Minimum:", min_val)
✅ 4. Count Frequency of Each Character in a String
python
Copy
Edit
# Frequency Count of Characters

def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

# Example usage
text = input("Enter a string: ")
print("Character Frequencies:")
for char, count in char_frequency(text).items():
    print(f"{char} : {count}")
✅ 5. Generate Multiplication Table of a Number
python
Copy
Edit
# Multiplication Table

def print_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

# Example usage
num = int(input("Enter a number: "))
print_table(num)
✅ 6. Check Leap Year
python
Copy
Edit
# Check Leap Year

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example usage
y = int(input("Enter a year: "))
print("Leap Year" if is_leap_year(y) else "Not a Leap Year")
✅ 7. Print Pattern – Right-Angled Triangle
python
Copy
Edit
# Print Triangle Pattern

def print_triangle(n):
    for i in range(1, n+1):
        print("*" * i)

# Example usage
rows = int(input("Enter number of rows: "))
print_triangle(rows)
✅ 8. Convert Decimal to Binary
python
Copy
Edit
# Decimal to Binary Conversion

def decimal_to_binary(n):
    return bin(n)[2:]

# Example usage
num = int(input("Enter a decimal number: "))
print("Binary:", decimal_to_binary(num))
✅ 9. Find Largest of Three Numbers
python
Copy
Edit
# Largest of Three Numbers

def largest_of_three(a, b, c):
    return max(a, b, c)

# Example usage
x, y, z = map(int, input("Enter three numbers: ").split())
print("Largest:", largest_of_three(x, y, z))
✅ 10. Print Fibonacci Series Using Recursion
python
Copy
Edit
# Recursive Fibonacci Series

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Example usage
terms = int(input("Enter number of terms: "))
print("Fibonacci Series:")
for i in range(terms):
    print(fibonacci(i), end=' ')
Would you like me to combine all 27 programs (earlier + these) into one .py file or .txt version for download and printing?

Also, do you want a few File Handling, OOP, or List/Dictionary-based problems added too for complete semester coverage?











Tools



ChatGPT can make m