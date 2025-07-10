# Program to write three lines of data into a file

# Open file in write mode
with open("sample_data.txt", "w") as file:
    file.write("This is line 1\n")
    file.write("This is line 2\n")
    file.write("This is line 3\n")

print("✅ Data written to sample_data.txt")
