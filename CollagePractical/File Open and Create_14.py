# Program to open file if exists, else create and write to it

filename = input("Enter the filename: ")

try:
    # Try to open the file in read mode
    with open(filename, "r") as file:
        content = file.read()
        print("📄 File Content:")
        print(content)
except FileNotFoundError:
    # If file doesn't exist, create it and write a line
    with open(filename, "w") as file:
        file.write("File is opened in write mode.\n")
    print(f"📝 File '{filename}' created and message written.")
