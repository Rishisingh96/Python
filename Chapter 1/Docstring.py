# Function with a Docstring.
def get_prime_number():
    """Getting the list of prime numbers between 1 to 20."""


get_prime_number();

# Function with a Docstring.
def getSum(x, y):
    """This is a docstring
This method takes two argument values and returns the summation of it."""
    print("Sum = ", (x + y))
getSum(20, 40) # Calling function.
print(getSum.__doc__) # Calling __doc__ method to print docstring.


# Function with a Docstring.
def getSquare(num):
    '''This method takes a number and returns the square of its value.'''
    return num*num;
print(getSquare.__doc__) # Calling __doc__ method to print docstring.
sq_value = getSquare(20);
print(sq_value);


class Rectangle:
    """
    This is a class for calculating the area of a rectangle.
Parameters:
        l (int) : The length of rectangle.
        b (int) : The breadth of rectangle.
    """
print(Rectangle.__doc__)
