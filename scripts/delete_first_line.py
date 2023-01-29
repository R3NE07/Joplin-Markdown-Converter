import os

# specify the directory where you want to look for .md files
directory = "C:/Users/rmeis/Dropbox/Apps/Obsidian"

# use os.walk() to get a list of all files in the directory and its subdirectories
for dirpath, dirnames, filenames in os.walk(directory):
    for file in filenames:
        # check if the file is a .md file
        if file.endswith(".md"):
            print(file)
            # construct the full path to the file
            file_path = os.path.join(dirpath, file)
            # open the file
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
            # delete the first line
            lines = lines[1:]
            # open the file for writing
            with open(file_path, 'w', encoding='utf-8', errors='ignore') as f:
                f.writelines(lines)

print("The first line of all .md files have been deleted.")