# Token Types: Keywords, Identifiers, Literals, Operators, Delimiters

# 1. Keywords and Identifiers
class Student:                           # 'class' is a Keyword, 'Student' is an Identifier
    def __init__(self, name, age):      # 'def' is a Keyword, '__init__', 'self', 'name', 'age' are Identifiers
        self.name = name                # '.' is a Delimiter, '=' is an Operator
        self.age = age

    def display_info(self):             # Method definition with Identifiers and Keywords
        print("Name:", self.name)       # 'print' is an Identifier, "Name:" is a String Literal
        print("Age:", self.age)

# 2. Literals (String, Integer, Float, Boolean)
student1 = Student("Rishi", 23)         # String & Integer Literals
student2 = Student("Anjali", 21)

# 3. Operators (Arithmetic, Comparison, Assignment)
total_age = student1.age + student2.age     # '+' is an Arithmetic Operator, '=' is an Assignment Operator
average_age = total_age / 2                 # '/' is an Arithmetic Operator

# 4. Boolean Literals and Comparison Operators
is_adult = student1.age >= 18               # '>=' is a Comparison Operator, Boolean result stored in Identifier

# 5. Using all together in function
def check_eligibility(student):
    if student.age >= 18:                   # 'if' is a Keyword, ':' is a Delimiter
        return True                         # 'True' is a Boolean Literal
    else:
        return False

# Function Calls and Output
student1.display_info()                     # Function call using '.'
print("Average Age:", average_age)
print("Is Student1 Adult?", check_eligibility(student1))
