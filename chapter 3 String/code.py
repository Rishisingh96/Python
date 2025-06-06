# String in Python
# Strings are a sequence of characters enclosed in quotes (single, double, or triple quotes).
# a = "Rishi singh" # Double quotes
# b= 'Rishi Singh' # Single quotes
# c ='''Rishi Singh''' # Triple quotes
# d = """Rishi Singh""" # Triple quotes
# print(a)
# print(b)   
# print(c)
# print(d)

# String concatenation
# str1 = "Hello"
# str2 = "World"
# str3 = str1 + " " + str2
# print(str3)  # Output: Hello World


# String formatting     
# name = "Rishi"
# age = 25

# First way to format string
# greeting = "Hello {name} singh. I am {age} years old.".format(name=name, age=age)

# Second way to format string
# greeting = f"Hello, my name is {name} and I am {age} years old."

# Third way to format string
# greeting = "Hello, my name is {} and I am {} years old.".format(name, age)

# Fourth way to format string
# greeting = "Hello, my name is %s and I am %d years old." % (name, age)

#  print(greeting)  # Output: Hello, my name is Rishi and I am 25 years old.


# String slicing
# my_string = "Hello, World!"
# print(my_string[0:5])  # Output: Hello
# print(my_string[7:])  # Output: World!  
# print(my_string[:5])  # Output: Hello
# print(my_string[-6:])  # Output: World!
# print(my_string[::2])  # Output: Hlo ol!
# print(my_string[::-1])  # Output: !dlroW ,olleH
# print(my_string[1:5:2])  # Output: el
# print(my_string[-5:-1])  # Output: World
# print(my_string[7:12])  # Output: World
# print(my_string[7:12:2])  # Output: Wrd
# print(my_string[::3])  # Output: Hoo ol!
# print(my_string[::-2])  # Output: !loW ,olH
# print(my_string[1:10:3])  # Output: el o
# print(my_string[::4])  # Output: Hoo!
# print(my_string[::-4])  # Output: !oW ,l
# print(my_string[1:10:4])  # Output: el
# print(my_string[::5])  # Output: H!

# SLICING WITH SKIP VALUE
my_string = "Hello, World!"
# print(my_string[0:5:2])  # Output: Hlo (skips every second character)
# print(my_string[::2])  # Output: Hlo ol! (skips every second character)
# print(my_string[::-1])  # Output: !dlroW ,olleH (reverses the string)

# find Total length of string
# print(len(my_string))  # Output: 13 (length of the string)


# String methods
'''# String methods are functions that perform operations on strings.
my_string = "Hello, World!"
print(my_string.lower())  # Output: hello, world!
print(my_string.upper())  # Output: HELLO, WORLD!
print(my_string.strip())  # Output: Hello, World! (removes leading and trailing whitespace)
print(my_string.replace("World", "Python"))  # Output: Hello, Python!
print(my_string.split(","))  # Output: ['Hello', ' World!']
print(my_string.find("World"))  # Output: 7 (index of the first occurrence of "World")
print(my_string.count("o"))  # Output: 2 (count of occurrences of "o")
print(my_string.startswith("Hello"))  # Output: True
print(my_string.endswith("!"))  # Output: True
print(my_string.isalpha())  # Output: False (contains non-alphabetic characters)
print(my_string.isalnum())  # Output: False (contains non-alphanumeric characters)
print(my_string.isdigit())  # Output: False (contains non-digit characters)
print(my_string.islower())  # Output: False (contains uppercase characters)
print(my_string.isupper())  # Output: False (contains lowercase characters)
print(my_string.isspace())  # Output: False (contains non-whitespace characters)
print(my_string.title())  # Output: Hello, World! (capitalizes the first letter of each word)
print(my_string.capitalize())  # Output: Hello, world! (capitalizes the first letter of the string)
print(my_string.swapcase())  # Output: hELLO, wORLD! (swaps the case of each letter)
print(my_string.zfill(20))  # Output: 0000000000Hello, World! (pads the string with zeros to a total width of 20)
print(my_string.center(20))  # Output:     Hello, World!      (centers the string within a width of 20)
print(my_string.ljust(20))  # Output: Hello, World!     (left-aligns the string within a width of 20)
print(my_string.rjust(20))  # Output:     Hello, World! (right-aligns the string within a width of 20)
print(my_string.expandtabs(4))  # Output: Hello, World! (expands tabs to spaces, if any)
print(my_string.splitlines())  # Output: ['Hello, World!'] (splits the string into lines)
print(my_string.partition(","))  # Output: ('Hello', ',', ' World!') (partitions the string into three parts based on the delimiter)
print(my_string.rsplit(","))  # Output: ['Hello', ' World!'] (splits the string from the right based on the delimiter)
print(my_string.split(", ", 1))  # Output: ['Hello', 'World!'] (splits the string into two parts based on the delimiter)
print(my_string.join(["Hello", "World"]))  # Output: Hello, World! (joins the elements of the list with the string as a separator)
print(my_string.count("o", 0, 5))  # Output: 1 (counts occurrences of "o" in the specified range)
print(my_string.index("World"))  # Output: 7 (index of the first occurrence of "World")
print(my_string.rindex("o"))  # Output: 4 (index of the last occurrence of "o")
print(my_string.rfind("o"))  # Output: 4 (index of the last occurrence of "o")
print(my_string.isnumeric())  # Output: False (contains non-numeric characters)
print(my_string.isidentifier())  # Output: False (not a valid identifier)
print(my_string.isprintable())  # Output: True (contains printable characters)
print(my_string.isascii())  # Output: True (contains only ASCII characters)
print(my_string.isdecimal())  # Output: False (contains non-decimal characters)
print(my_string.isnumeric())  # Output: False (contains non-numeric characters)

'''
