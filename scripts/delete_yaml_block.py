import os

# specify the directory where you want to look for .md files
directory = "C:/Users/rmeis/Dropbox/Apps/Obsidian"

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
            with open(file_path, 'w', encoding='utf-8', errors='ignore') as f:
                in_block = False
                for line in lines:
                    if '---' in line:
                        in_block = not in_block
                        continue
                    if not in_block:
                        f.write(line)
                        
print("All YAML blocks have been deleted.")
