__author__ = 'svizor'

import os
import ast


def scaner():

    wotch_dir = "/Users/svizor/PycharmProjects/testing/dpx_sources"
    #raw_input("Enter source Directory:")
    file_ext = ".dpx"
    #"." + raw_input("Enter extention:")
    files_dict = {}

    f = open("files_dict.txt", "r+")

    if os.path.getsize("files_dict.txt") > 0:
        files_dict = ast.literal_eval(f.read())

    for (dirname, dirs, files) in os.walk(wotch_dir):
        for filename in files:
            if filename.endswith(file_ext):
                if filename not in files_dict.keys():
                    print filename

    f.close()

scaner()


"""
output_dir = raw_input("Enter destination Directory:")

def script_writer():

    files_list = {}
    files_list.update(scaner())

    clip_range = [i for i in range(clip_in, clip_out)]
    my_clip_range = []

    for a in clip_range:
        if a in files_list:
            my_clip_range.append(output_dir + "/"+ a)
    return my_clip_range

print script_writer()



clip = "MVI_8055"
clip_in = 604
clip_out = 633


def reading(self):
    s = open('deed.txt', 'r').read()
    self.whip = eval(s)
"""
