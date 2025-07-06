'''num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

greatest_num = (num1 if (num1>num3) else num3) if(num1>num2)else(num2 if (num2>num3)else num3)
print("The greatest number is: ", str(greatest_num))
'''

'''x, y = 20, 40
z = 20 if (x > y) else 40
print("Greatest number: ", z)'''

'''age = int(input("How old are you ?"))
eligible = "You are eligible to vote" if(age>=18) else "You are not eligible to vote."
print(eligible)'''

# Nested Ternary Operator Example
'''num1, num2 = 10, 20
# Nested ternary operator.
num = "num1 = num2" if(num1 == num2) else "num1 > num2" if(num1 > num2) else "num2 > num1"
print(num)'''

# Python program to find greater between three numbers.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
if num1 > num2 and num1 > num3:
    print(num1, 'is a greater number among the three numbers.')
elif num2 > num1 and num2 > num3:
    print(num2, 'is a greater number among the three numbers.')
else:
    print(num3, 'is a greater number among the three numbers.')

