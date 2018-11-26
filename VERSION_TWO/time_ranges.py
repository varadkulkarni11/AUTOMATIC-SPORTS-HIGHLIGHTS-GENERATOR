import math
import subprocess
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from os import system
import os

frames =[]
frame_ranges=[]
time_ranges=[]
with open('histogram_frame_numbers2.txt','r') as f:
    for line in f:
        words = line.split()
        for i in words:
            frames.append(int(i))
sz=len(frames)
i=0
while i<(sz-1):
    j=i
    st=frames[i]
    while (j<sz-1 and ((frames[j+1]-frames[j])==1)  ):
      j+=1
    en=frames[j]
    i=j
    i+=1
    frame_ranges.append((st,en))
for i in frame_ranges:
    a,b=i
    a=round(a/30) #fps is 30
    b=round(b/30)
    t=(math.floor(max(a,0)),math.ceil(min(b,12600)))
    time_ranges.append(t)
#making time ranges disjoint
ranges=[]
i=0
sz=len(time_ranges)
god =[0]*12601
for i in time_ranges:
    x,y=i
    for j in range(x,y+1):
        god[j]=1
i=0
while i<12601:
    if god[i]==0:
        i+=1
        continue
    st=i
    j=i
    while god[j] and j<=12600:
       j+=1
    en=j
    i=j
    i+=1
    ranges.append((st,en))
max_idx=len(ranges)
print(max_idx)

f=open('v2_time_ranges.txt','w')
for i in ranges:
    x,y=i
    c=str(x)+' '+str(y)
    f.write(c+'\n')
f.close()

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
            print('fuckthis1')
        try:
            os.remove("D:/BEPROJECT/tempp/highlights.ts")
        except:
            print('fuckthis2')
        try:
            os.remove("D:/BEPROJECT/tempp/temp_video.mp4")
        except:
            print('fuckthis3')
        try:
            os.remove("D:/BEPROJECT/tempp/temp_video.ts")
        except:
            print('fuckthis4')
        try:
            os.rename('D:/BEPROJECT/tempp/main_out_temp.mp4','D:/BEPROJECT/tempp/highlights.mp4')
        except:
            print('fuckthis5')
