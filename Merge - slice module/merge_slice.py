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
    z=y-x
    name="D:/BEPROJECT/tempp/highlights"+str(i)+".mp4"
    command="ffmpeg -ss "+str(x)+".0 -i match.mp4 -t "+str(z)+" "+name
    subprocess.call(command, shell=True)
clips=[]
for i in range (0,max_idx):
    name="D:/BEPROJECT/tempp/highlights"+str(i)+".mp4"
    clips.append(VideoFileClip(name))
final_clip = concatenate_videoclips(clips)
final_clip.write_videofile("v2_highlights.mp4")

