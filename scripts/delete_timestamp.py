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
                # flag to check if inside yaml block
                in_yaml_block = False
                # new lines to write to file
                new_lines = []
                for line in lines:
                    if line.strip() == '---':
                        in_yaml_block = not in_yaml_block
                        new_lines.append(line)
                    elif not in_yaml_block or not (line.startswith('updated:') or line.startswith('created:')):
                        new_lines.append(line)
            # open the file and write the new lines
            with open(file_path, 'w', encoding='utf-8', errors='ignore') as f:
                f.writelines(new_lines)

print("All timestamps inside YAML blocks have been deleted.")
