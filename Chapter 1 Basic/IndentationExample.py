# Declare a user-defined function.
def display():
# Below two lines of code are the part of the function.
  var = "Scientech Easy" # This statement is indented by two spaces.
  print(var) # this print statement is indented by two spaces.
# Below is the code to call a function named display().
display()

# --------------------------------------------------------------------------------------------------------------------------------
name = 'Ivaan'
if name == 'Ivaan':
    print('WelCome Ivaan..') # Intended by four spaces by default.
    print('How are you, today?') # # Intended by four spaces by default.
else:
    print('Dude! whoever are you ') # Intended by four spaces by default.
    print('Why are you here?') # Intended by four spaces by default.
print('I am fine, thank you!')
print('Have a nice day!')

# --------------------------------------------------------------------------------------------------------------------------------

# Wrong Indentation Error:
# if(6 > 3):
# print("6 is greater than 3") # Here, we have skipped indentation space before the print statement.

# --------------------------------------------------------------------------------------------------------------------------------

# With Correct Indentation:
if(6 > 3):
    print("6 is greater than 3") # Here, we have indented with four spaces.

# --------------------------------------------------------------------------------------------------------------------------------

# Mismatch Indentation:
# a = 10
# b = 20
# c = 30
# if(b > a):
#   print("b is greater than a")
#     print("b is greater than a but less than c")

# --------------------------------------------------------------------------------------------------------------------------------

# Correct Indentation:
a = 10
b = 20
c = 30
if(b > a):
    print("b is greater than a")
    print("b is greater than a but less than c")
