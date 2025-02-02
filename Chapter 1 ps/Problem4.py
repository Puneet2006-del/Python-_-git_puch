import os

def list_directory_contents(directory_path):
    try:
        # Get a list of files and subdirectories in the specified directory
        contents = os.listdir(directory_path)
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Directory '{directory_path}' does not exist.")
    except PermissionError:
        print(f"Permission denied for directory '{directory_path}'.")

# Example usage:
directory_path = "/Windows"
list_directory_contents(directory_path)
 