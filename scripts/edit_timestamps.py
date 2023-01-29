import os
import time
import pywintypes
import win32file

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
                for i, line in enumerate(lines):
                    if 'updated:' in line:
                        #extract the modification timestamp
                        modification_date = line.split(':')[1].strip() + ':00:00'
                        # convert the date string to a timestamp
                        modification_timestamp = time.mktime(time.strptime(modification_date, "%Y-%m-%d %H:%M:%S"))
                        # convert the timestamp to a FILETIME structure
                        modification_filetime = pywintypes.Time(modification_timestamp)
                    if 'created:' in line:
                        #extract the creation timestamp
                        creation_date = line.split(':')[1].strip() + ':00:00'
                        # convert the date string to a timestamp
                        creation_timestamp = time.mktime(time.strptime(creation_date, "%Y-%m-%d %H:%M:%S"))
                        # convert the timestamp to a FILETIME structure
                        creation_filetime = pywintypes.Time(creation_timestamp)
            # open the file and get the handle
            handle = win32file.CreateFile(file_path, win32file.GENERIC_WRITE, 0, None, win32file.OPEN_EXISTING, win32file.FILE_ATTRIBUTE_NORMAL, None)
            # change the creation and modification date of the file
            win32file.SetFileTime(handle, creation_filetime, None, modification_filetime)
            # close the handle
            win32file.CloseHandle(handle)
                
print("All .md files' creation and modification dates have been changed.")
