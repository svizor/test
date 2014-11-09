from timecode import Timecode

handle = 3
#raw_input("Enter media handle:")
filename = "MVI_8055"
my_clip_start = Timecode('24', '02:24:10:10')
_in = 604
_out = 633

print my_clip_start.frames

class Clip(object):
    def __init__(self, clipname, media_start, clip_in, clip_out):
        self.clipname = clipname
        self.media_start = media_start
        self.clip_in = clip_in
        self.clip_out = clip_out

my_clip = Clip(filename, my_clip_start, _in, _out)
my_clip_in = my_clip.clip_in + my_clip.media_start.frames - handle - 1
my_clip_out = my_clip.clip_out + my_clip.media_start.frames + handle
for a in range(my_clip_in, my_clip_out):
    print my_clip.clipname + "." + "%.8d" % a + ".ari"