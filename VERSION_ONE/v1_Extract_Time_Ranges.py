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

#CALCULATE AVERAGE AUDIO LEVEL OF ALL AUDIO FRAMES
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
thresh_hold=23*avg
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
ranges=[]
i=0
sz=len(time_ranges)
god =[0]*6901
for i in time_ranges:
    x,y=i
    for j in range(x,y+1):
        god[j]=1
i=0
while i<6901:
    if god[i]==0:
        i+=1
        continue
    st=i
    j=i
    while god[j] and j<=6900:
       j+=1
    en=j
    i=j
    i+=1
    ranges.append((st,en))
max_idx=len(ranges)

f=open('v1_time_ranges.txt','w')
for i in ranges:
    x,y=i
    c=str(x)+' '+str(y)
    f.write(c+'\n')
f.close()

