
# This is a single line
'''
I 
am
multiline 
comments
'''
print("Hello, World!")  # This is a single line comment
# This is also a single line comment

'''Types of Comments in Python
Comments are the important part of any program that helps to improve the readability and understanding of the complex program. In Python, there are mainly three types of comments. They are as:
	1. Single-line comment
	2. Inline comment
	3. Multiline comment
'''

# 1. Single-line comment

# msg is a method which will accept a parameter and print the value of it.
def msg(parameter):
    print(parameter)
msg('Welcome you to Scientech Easy!')

# 2. Inline comment
x = 100 # Here, x is an integer variable that stores the value 100. 


""" Python
program
to calculate
the sum of
three
numbers.
"""
# or
''' Python
program
to calculate
the sum of
three
numbers.
'''
"""Python
program
to calculate
the sum of
three
numbers.
"""
def sum(x, y, z):
    s = x + y + z
    print("Sum of three numbers = ", s)
sum(10, 20, 30) 
