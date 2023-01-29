# Joplin-Markdown-Converter  

## Introduction  

> This script was entirely written using ChatbotGPT as I was too lazy to learn python.  

When exporting Notes from Joplin, the Markdown files will have a creation timestamp of when you exported them, instead of the day you wrote those notes.  
When importing said .MD files to other note-taking apps (like Obsidian), you wont be able to sort them by date as a result.  
However, the real creation date is written inside the files in the YAML format.  
This python script looks for this timestamp inside the .MD files, extracts them and changes their metatags according to that date.  

The Markdown files exported from joplin should look like this:  
```
---  
title: My First Note  
updated: 2022-02-02 15:27:44Z  
created: 2022-02-01 08:02:19Z  
tags:  
  - protocol notes  
---  

This is my first note c:  
```

## Requirements  
- Tested on Windows only! (Linux handles metainformation differently)  
- Download the ###.py scripts  
- Install Python from the Microsoft Store*  
- In Joplin export your notes in the format `Markdown + Front Matter` (export a second backup just in case)  

## How to Use  
- Open the script with a text editor and change the directory to where the Markdown files were exported (replace all `\` with `/`)  
- Open the command line  
- install win32 module for python: `pip install pywin32`  
- move to the directory where the script is located: `cd C:\Users\your_username\Downloads\scripts`  
- execute script: `python ###.py`  
- Thats it!  

## Scripts  
- `edit_timestamps.py`: simply extracts the creation and modification date from inside your Markdown files and modifies their metatags accordingly (except minutes and seconds are set to 00 due to a bug)  
- `delete_timestamp_lines.py`: searches for the lines starting with `updated:` and `created:` inside the YAML block inside your Markdown files and deletes them  
- `delete_yaml_block.py`: deletes the entire YAML block inside the markdown files (useful for when your new Markdown App doesnt automatically hide it)  
- `delete_first_line.py`: deletes the first line of every .MD file (after removing the YAML block, the Markdown files are left with a single empty line at the top)
- [Here](https://github.com/R3NE07/Joplin-Markdown-Converter/blob/main/example_outputs.MD) you can see examples of what the scripts do  

## Notes  
- The script is unable to extract the hour and second from the timestamps and simply sets those to 00 in the metatags (just a workaround that I couldn't get ChatbotGPT to fix)  
- `Python was not found` is a common Windows issue. Sometimes after installing Python from their official website, the system environment variables are not set correctly, and the system cannot find the python executable. It can be fixed by adding the python executable path to the system environment variables. You can also try installing the Python from the Microsoft Store, which automatically sets up the environment variables and makes it easier to run Python scripts.  
