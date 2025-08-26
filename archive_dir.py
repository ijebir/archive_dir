import os
from file_dir import file_dir

max_uproot = 1
max_downroot = 1

file_list = []

# { "path": "", "file": "", "type": "", "isIgnore": False }

# We recursively to check the directory above root for files other folders
# Maybe define a max_depth for recursively looking into dir
def scan_directory(path):
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            #file_list.append(file(os.path.join(path, entry)))
            file_list.append(file_dir("..", entry, "file"))
            print(file_list[0])
            # Add to DS
        else:
            # Check if directory shoulde be included, if so traverse
            # otherwise skip it
            print("")

# Init
#print("This tool will archive into zip the contents of all files above this dir")
#if input("Proceed, y to continue, or any key otherwise: ") == "y":
#    print("Checking directories...")
#    scan_directory("./")
#else:
#    print("program closing")

#a = file("../", "./", "dir")
#print(a)

#a = file_dir(".", "a", "dir")
#b = file_dir("./a", "b", "file")
#print(a)
#print(b)

scan_directory("../")


# We need to provide the possibility of skipping a directory (all files will be included)
# What is the best way to store this info: (key, value) -> (directory_path, Boolean)

# We need to zip the files at root with correct date and