import os

# Specify the directory path
directory_path = '/'  # Replace with your directory path

# Get the list of files and directories
contents = os.listdir(directory_path)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)

