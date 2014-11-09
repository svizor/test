__author__ = 'svizor'

import os
import ast


def source_scaner():

    wotch_dir = raw_input("Enter source Directory:")
    file_ext = "." + raw_input("Enter extention:")

    files_dict = {}
    f = open("files_dict.txt", "r+")

    if os.path.getsize("files_dict.txt") > 0:
        files_dict = ast.literal_eval(f.read())

    f.truncate()
    f.close()

    f = open("files_dict.txt", "r+")

    for (dirname, dirs, files) in os.walk(wotch_dir):
        for filename in files:
            if filename.endswith(file_ext):
                if filename not in files_dict.keys():
                    thefile = os.path.join(dirname, filename)
                    files_dict.update({filename: thefile})

    f.write(str(files_dict))
    f.close()

source_scaner()