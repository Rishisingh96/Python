# Program to classify age group

# Taking age input from user
age = int(input("Enter age of the person: "))

# Classifying based on age
if age <= 1:
    print("Category: Infant 👶")
elif age > 1 and age < 13:
    print("Category: Child 🧒")
elif age >= 13 and age <= 19:
    print("Category: Teenager 👦")
else:
    print("Category: Adult 🧑")
