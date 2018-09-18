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
##CALCULATE AVERAGE AUDIO LEVEL OF ALL AUDIO FRAMES
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
#GETTING TIME FRAMES WHERE AUDIO AMPLITUDE > THRESHHOLD
thresh_hold=25*avg
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
    while data>thresh_hold and j<=length:
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
        if x<y :
            time_ranges.append(t)
    i+=1
##MAKING TIME RANGES DISJOINT
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
