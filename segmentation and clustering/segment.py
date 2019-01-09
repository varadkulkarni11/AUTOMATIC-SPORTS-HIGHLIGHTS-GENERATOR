import subprocess
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *
from PIL import Image
import cv2

cap = cv2.VideoCapture("ball4.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)      # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = frameCount/fps
ranges=[]


ini_st=0.0
ini_en=ini_st
seg_count=2*int(duration)
for i in range (0,seg_count):
    ranges.append((ini_st,ini_en))
    ini_st+=0.5

#SLICING VIDEO IN TIME RANGES AND THEN FINALLY MERGING TO GET FINAL VIDEO OUTPUT
max_idx=len(ranges)
for i in range (0,max_idx):
    x,y=ranges[i]
    name="segments4/"+str(i)+".mp4"
    command="ffmpeg -ss "+str(x)+" -i ball4.mp4 -t 00:00:00.50 "+name
    subprocess.call(command, shell=True)

