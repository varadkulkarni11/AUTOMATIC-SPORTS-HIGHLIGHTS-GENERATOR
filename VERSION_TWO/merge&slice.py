import subprocess
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from os import system
import os
ranges=[]
with open('v2_time_ranges.txt','r') as f:
    for line in f:
        words = line.split()
        x,y=words
        xx=int(x)
        yy=int(y)
        ranges.append((xx,yy))
#SLICING VIDEO IN TIME RANGES AND THEN FINALLY MERGING TO GET FINAL VIDEO OUTPUT
max_idx=len(ranges)
for i in range (0,max_idx):
    x,y=ranges[i]
    if i==0:
        name="D:/BEPROJECT/tempp/highlights.mp4"
        ffmpeg_extract_subclip("match.mp4", x, y, targetname=name)
    else:
        name="D:/BEPROJECT/tempp/temp_video.mp4"
        ffmpeg_extract_subclip("match.mp4", x, y, targetname=name)
        cmd = "ffmpeg -i D:/BEPROJECT/tempp/temp_video.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts D:/BEPROJECT/tempp/temp_video.ts"
        system(cmd)
    if i!=0:
        cmd = "ffmpeg -i D:/BEPROJECT/tempp/highlights.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts D:/BEPROJECT/tempp/highlights.ts"
        system(cmd)
        concat_str="D:/BEPROJECT/tempp/highlights.ts"+"|"+"D:/BEPROJECT/tempp/temp_video.ts"
        cmd=cmd = """ffmpeg -i "concat:{0}" -c copy -bsf:a aac_adtstoasc D:/BEPROJECT/tempp/main_out_temp.mp4""".format(concat_str)
        system(cmd)
        try:
            os.remove("D:/BEPROJECT/tempp/highlights.mp4")
        except:
            print('fuckthis')
        try:
            os.remove("D:/BEPROJECT/tempp/highlights.ts")
        except:
            print('fuckthis')
        try:
            os.remove("D:/BEPROJECT/tempp/temp_video.mp4")
        except:
            print('fuckthis')
        try:
            os.remove("D:/BEPROJECT/tempp/temp_video.ts")
        except:
            print('fuckthis')
        try:
            os.rename('D:/BEPROJECT/tempp/main_out_temp.mp4','D:/BEPROJECT/tempp/highlights.mp4')
        except:
            print('fuckthis')
