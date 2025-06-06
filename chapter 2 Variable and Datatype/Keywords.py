# Python Operator Keywords – and, or, not, in, is
'''print(True and True)
print(True and False and True)
print(True and 1)'''

'''print(True or True)
print(False or False or True)
print(True or False)
print(True or 1)'''

'''print(not True)
print(not False)'''

'''num = [10,20,30,40,50]
print(50 in num)  # True in check Between 50 and num , if 50 is present then True else False
print(60 in num)'''

'''print(True is True)
print(False is True)
print(None is None)
print((2+4) is (3*2))
print((4+3) is (3*2))  # False

print("\n")
print( ' ' == ' ' )
print( ' ' is ' ' )
print( () == () )
print( () is () )

print("\n")
print( [ ] == [ ] )
print( [ ] is [ ] )  
print( { } == { } )
print( { } is { } )'''



# Python Iteration Keywords – for, while, break, continue
''' for count in range (1,4):
     print(count,"Rishi singh")'''


'''count = 0;
while(count<3):
    print(count,"Rishi singh")
    count = count+1;
print("While loop ended !")'''

'''for i in range(1,5):
    if(i==3):
        break
    print(i,"Rishi singh")'''

'''for i in range(1,6):
    if(i==4):
        continue
    print(i,"Rishi singh")'''

# def keyword
'''def func():
    print("Inside function")

func()'''

# Python Return Keywords – Return, and Yield
'''def func_return():
    x = 20
    return x

def func_no_return():
    x = 50

print(func_return())
print(func_no_return())'''


'''yield: We use yield keyword inside a function like a 
return statement but yield returns a generator object to 
the caller rather than a data value. An example code is as:'''
'''def func():
    x = 0
    for i in range(5):
        x=x+ i;
        yield x
for i in func():
    print(i)'''

# Lambda keyword
'''cube = lambda x:x*x*x;
print("Cube is : ",cube(7))'''

'''my_var1 = 200
my_var2 = "Scientech Easy"
# check if my_var1 and my_var2 exists.
print(my_var1)
print(my_var2)
# delete both the variables.
del my_var1
del my_var2
# check if my_var1 and my_var2 exists
print(my_var1)
print(my_var2)'''



# Python Exception Handling Keywords – try, except, raise, and finally

'''# initializing the value of variables.
x = 10
y = 0
# No exception raised in try block
try:
    z = x // y  # raises divide by zero exception.
    print(z)
# handles zero division exception
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    # this block always gets executed regardless of exception produced.
    print('finally block always gets executed')'''



