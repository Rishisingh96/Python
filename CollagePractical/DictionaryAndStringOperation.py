#Dictionary Operation
student = {
    "name":"Rishi",
    "age" : 20,
    "course": "MCA"
}

print("Student Type :", type(student))

print("Original Dictionary : ", student)

#Add (append) a new key-value pair
student["university"] = "SAGE University"
print("After adding university:", student)

#Update existing value
student["age"] = 23
print("After updating age:", student)

#Remove a key
student.pop("course")
print("After removing course:", student)

#