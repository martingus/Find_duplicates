"""Find duplicates in a give directory (and sub-directories)"""
import os
# 1 get active directory
cwd = os.getcwd()
# 2 get sub-directories, append path to a list
dirlist = []

# 3 for each sub-dir: 
    # 4 repeat 2 and 3
# 5 for each dir in list: 
    # 6 list all files and save filename, create, last_mod, size and path in a new list
# 7 sort the list per filename
# 8 loop through the list. For each duplicate, move data to a new list, suggest 'k' or 'd' for keep or delete based on last-mod-date
# 9 Save this as excel-file 