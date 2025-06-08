# Multiple Assignment
'''x = y = z = 20
print(id(x))
print(id(y))
print(id(z))

x, y, z = 20, 25.50, 'text'
print(id(x))
print(id(y))
print(id(z))'''

# How to Determine Data type of Variables in Python?
'''num = 100
print(type(num))'''


# How to determine the type of variable in Python?
'''num1 = 50
num2 = 20.50
num3 = 3.5 + 7.5j
print(type(num1))
print(type(num2))
print(type(num3))
# Checking an object belongs to a particular class.
print(isinstance(num3, complex))'''


def func(x):
    value = (x + 5) * 10
    return value
x = 10
final_value = func(x)
print("Final value = ", final_value)

