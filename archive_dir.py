import os

# { "path": "", "file": "", "type": "", "isIgnore": False }

# We recursively to check the directory above root for files other folders
def scan_directory(path):
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            print(path, entry)

# We need to provide the possibility of skipping a directory (all files will be included)
# What is the best way to store this info: (key, value) -> (directory_path, Boolean)

# We need to zip the files at root with correct date and