import numpy as np
import cv2
from matplotlib import pyplot as plt
import subprocess
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *
from PIL import Image
cap = cv2.VideoCapture("ball3.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)      # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = frameCount/fps
seg_count=2*int(duration)
Z = []
for i in range (0,seg_count):
    cap = cv2.VideoCapture('segments3/'+str(i)+'.mp4')    
    cap.set(2, 0)
    res, frame = cap.read()
    #cv2.imshow('lol',frame)
    dumy=np.array(100000*i)
    histo = cv2.calcHist([frame],[0],None,[256],[0,256])
    pushh=np.append(dumy,histo)
    Z.append(pushh)
# convert to np.float32

Z = np.float32(Z)
klusters=5
criteria = (cv2.TERM_CRITERIA_MAX_ITER, 10, 1.000)
ret,label,center=cv2.kmeans(Z,klusters,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

labelmap=[]
for i in range (0,klusters):
    tempo=[]
    for j in range (0,seg_count):
        if label[j]==i:
           tempo.append(j)
    labelmap.append(tempo)
labelmap.sort()
for i in range (0,klusters):
    clips=[]
    for j in range (0,len(labelmap[i])):
        name='segments3/'+str(labelmap[i][j])+'.mp4'
        clips.append(VideoFileClip(name))
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile('CLUSTERS3/cluster'+str(i)+'.mp4')
                             
                 


