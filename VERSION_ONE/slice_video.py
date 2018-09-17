import wave, struct
import cv2
import numpy as np
import math
import subprocess

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
##avg=511.0
print('average values calculated now finding ranges: ')
print(avg)
i=0
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
    z=0
    if ff==1:
    		x,y=t
        
        ss1=x%60
        mm1=x/60
        hh1=mm1/60
        mm1=mm1%60


        ss2=y%60
        mm2=y/60
        hh2=mm2/60
        mm2=mm2%60

        a='"'+str(hh1)+':'+str(mm1)+':'+str(ss1)+'"'
        b='"'+str(hh2)+':'+str(mm2)+':'+str(ss2)+'"'
        outputfilename="/temp/output"+str(z)+".mp4"
        ffmpeg_command1 = ["ffmpeg", "-i", "matchsample.mp4", "-acodec", "copy", "-ss", a, "-t", b, outputfilename]
        subprocess.call(ffmpeg_command1)
        z+=1
        #print(t,file=open("god_attempt10.txt","a"))
    i+=1

    
    
