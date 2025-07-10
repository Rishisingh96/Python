# Improved program with IOError handling

filename = input("Enter the filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
        print("📄 File Content:")
        print(content)

except FileNotFoundError:
    try:
        with open(filename, "w") as file:
            file.write("File is opened in write mode.\n")
        print(f"📝 File '{filename}' created successfully.")
    except IOError:
        print("❌ IOError occurred while trying to create the file.")

except IOError:
    print("❌ IOError occurred while trying to read the file.")
