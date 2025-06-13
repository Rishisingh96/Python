'''# Initialization: The variable count has defined outside the loop and will update inside the loop.
count = 0
# Declare the while loop statement.
# Loop continuation condition expression that must ends with a colon (:).
while count < 5:
# Body of the loop.
    print('Hello Python') # This statement will execute as long as the condition is true.
    count += 1 # It counts the number of executions, and increments count by 1.
print('Loop finished.') # Continue program if the condition is false.
'''

'''i=1;
while i<5:
    print('Current value of i is : ',i)
    i = i+1;'''

'''Let’s write a program in Python using while loop to find the Fibonacci series of numbers till 30. The Fibonacci series is: 0, 1, 1, 2, 3, 5, 8, 13, . . . .
'''

'''num1 = 0
num2 = 1
temp = 0

print('Fibonacci series of numbers till 30 are:')
print("Fibonacci Series is : ",num1, num2,end='')
while(num2<21):
    next = num1 + num2
     # num1, num2 = num2, num1+num2
    print(next,end='')
    num1 = num2 
    num2 = next;'''

row = int(input('Enter the number of rows:'))
while row>=0:
    x = '*' *row
    print(x)
    row = row-1;

'''💡 Dry Run with Example Input:
Suppose the user enters:

sql
Copy code
Enter the number of rows: 4
So initially:
row = 4

Now the loop runs while row >= 0.

🔁 Step-by-Step Execution:
Iteration	row Value	'*' * row	Output	After row = row - 1
1	4	****	****	3
2	3	***	***	2
3	2	**	**	1
4	1	*	*	0
5	0	'' (empty)	(blank)	-1
6	-1	loop ends		

✅ Final Output:
markdown
Copy code
****
***
**
*
(The last line is blank because of '*' * 0.)

🔚 Conclusion:
The program prints a reverse pyramid of stars from the entered number down to 0.
Let me know if you want to skip the blank line or print a forward pattern instead!'''