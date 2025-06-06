import os

directory_path = '/'
contents = os.listdir(directory_path)
for item in contents:
    print(item)
# # Function to print the contents of a directory
# def print_directory_contents(directory):
#     try:
#         # List all files and directories
#         contents = os.listdir(directory)
#         print(f"Contents of '{directory}':")
#         for item in contents:
#             print(item)
#     except FileNotFoundError:
#         print(f"The directory '{directory}' does not exist.")
#     except PermissionError:
#         print(f"Permission denied to access '{directory}'.")

# # Specify the directory
# directory_path = input("Enter the path of the directory: ")

# # Print the contents of the specified directory
# print_directory_contents(directory_path)
