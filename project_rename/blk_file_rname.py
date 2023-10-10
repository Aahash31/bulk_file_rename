"""
Goal: Rename file or files in a directory
Purpose: To understand os library and it's capabilties
"""


# import os allows functions for interecting with operating system
import os

def rename_file():
    i  = 0
    # Copied path of directory containing files to be renamed
    path = "/Users/aahashsuthahar/Documents/Projects/Python/images/"
    
    """
    listdir() returns a list of all files and directories
    in current directory

    """
    for filename in os.listdir(path):
        new_name = "img" + str(i) + ".png"
        original = path + filename
        new_name_path = path + new_name
        os.rename(original,new_name_path)
        i += 1
    
if __name__ == '__main__':
    rename_file()
