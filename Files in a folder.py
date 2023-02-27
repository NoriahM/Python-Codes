import os

def list_files_in_directory(path):
    # Use the 'os' module to get a list of files in a directory
    files = os.listdir(path)
    
    # Print each file in the list
    for file in files:
        print(file)

# Prompt the user for a directory path
path = input("Enter a directory path: ")

# Call the 'list_files_in_directory' function and pass the user-specified path
list_files_in_directory(path)


