from timecode import Timecode

"""
import os
import ast
"""

edit_clip = ["MVI_8055", '24', '00:00:00:00', 613, 619]


def clip():
    #filename, rate, tc_media_start, _in, _out
    handle = 3
    #raw_input("Enter media handle:")
    filename = edit_clip[0]
    rate = edit_clip[1]
    tc_media_start = edit_clip[2]
    _in = edit_clip[3]
    _out = edit_clip[4]
    media_start = Timecode(rate, tc_media_start)
    my_clip_in = _in + media_start.frames - handle - 1
    my_clip_out = _out + media_start.frames + handle
    for a in range(my_clip_in, my_clip_out):
        print filename + "." + "%.8d" % a + ".ari"

clip()
"""
edit_dict = {}

fs = open("edit_dict.txt", "r")
if os.path.getsize("edit_dict.txt") > 0:
    edit_dict = ast.literal_eval(fs.read())

print edit_dict
fs.close()


for i in edit_dict.keys():
    clip(filename, my_clip_start, _in, _out)
"""