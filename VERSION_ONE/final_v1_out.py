import wave, struct
import cv2
import numpy as np
import math
import subprocess
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from os import system
import os
def bytes_to_int(bytes):
    result = 0
    for b in bytes:
        result = result * 256 + int(b)
    return result

waveFile = wave.open('main_audio.wav', 'r')

length=waveFile.getnframes()
avg=0.0
sum=0.0
fps=44100
for i in range(0,length):
    waveData = waveFile.readframes(1)
    temp=bytes_to_int(waveData)
    if temp!=0:
        data=struct.unpack('<hh',waveData)[0]
    else:
        data=0
    data=data*1.0
    sum+=abs(data)
avg=sum/length
avg/=2
i=0
time_ranges=[]
while i<=length:
    waveData = waveFile.readframes(1)
    temp=bytes_to_int(waveData)
    if temp!=0:
        data=struct.unpack('<hh',waveData)[0]
    else:
        data=0
    data=data*1.0
    time=i/fps
    a=time
    j=i
    ff=0
    while data>25*avg and j<=length:
        ff=1
        waveData = waveFile.readframes(1)
        temp=bytes_to_int(waveData)
        if temp!=0:
            data=struct.unpack('<hh',waveData)[0]
        else:
            data=0
        data=data*1.0
        j+=1
    i=j
    b=i/fps
    t=(math.floor(max(a-10,0)),math.ceil(min(b+10,12600)))
    if ff==1:
        x,y=t
        if x<y
            time_ranges.append(t)
    i+=1
start_time=[0]*12601
end_time=[0]*12601
god=[0]*12601
max_idx=len(time_ranges)
for i in range (0,max_idx):
    x,y=time_ranges[i]
    start_time[x]+=1
    end_time[y]+=1
cur=0
c=0
for i in range (0,12601):
    if start_time[i]!=0:
        cur+=1
    if cur!=0:
        god[i]=1
    if end_time[i]!=0:
        cur-=1
ranges=[]
i=0
while i<=12600:
    j=i
    f=0
    while god[j]==1 and j<12600:
        j+=1
        f=1
    if f==1:
        c+=1
        ranges.append((i,j-1))
    i=j
    i+=1
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
        os.remove("D:/BEPROJECT/tempp/highlights.mp4")
        os.remove("D:/BEPROJECT/tempp/highlights.ts")
        os.remove("D:/BEPROJECT/tempp/temp_video.mp4")
        os.remove("D:/BEPROJECT/tempp/temp_video.ts")
        os.rename('D:/BEPROJECT/tempp/main_out_temp.mp4','D:/BEPROJECT/tempp/highlights.mp4')
print (max_idx)
