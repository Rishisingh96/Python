rows = 5  # You can take input from user too

print("Right-Angled Triangle (Increasing Stars)\n")

for i in range(1, rows + 1):          # Outer loop for rows
    for j in range(1, i + 1):         # Inner loop for columns
        print('*', end='')            # Print star on same line
    print()                           # Move to next line


'''Explanation (Java-style Logic in Python):
Java Concept	Python Equivalent
for (int i = 1; i <= n; i++)	for i in range(1, rows + 1)
System.out.print("*");	print("*", end="")
System.out.println();	print()'''

'''
Dry Run Table:
We’ll trace the values of i, j, and output printed at each step:

Iteration (i)	Inner Loop (j) Values	Printed Output	Explanation
i = 1	j = 1	*	Only 1 star on first row
i = 2	j = 1, 2	**	2 stars on second row
i = 3	j = 1, 2, 3	***	3 stars on third row
i = 4	j = 1, 2, 3, 4	****	4 stars on fourth row
i = 5	j = 1, 2, 3, 4, 5	*****	5 stars on fifth row

Each time after printing stars in the inner loop, print() moves to the next line.

✅ Final Output:
markdown
Copy code
*
**
***
****
*****
🧠 Summary:
Outer loop controls the row number

Inner loop prints stars equal to the current row number

Looks just like a right-angled triangle (left-aligned)
'''