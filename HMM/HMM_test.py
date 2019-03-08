import numpy as np
from hmmlearn import hmm
from sklearn.externals import joblib
import subprocess
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *
from PIL import Image
import cv2
events=["aerial","BoundaryLine","runup","runupp"]
fname="runup"
event_count=len(events)

capp=cv2.VideoCapture("BoundaryLine/1.mp4")
fc = int(capp.get(cv2.CAP_PROP_FRAME_COUNT))
for i in range(0,fc):
    capp.set(1,i)
    ress,framee=capp.read()
    #framee = framee[(235):900, 400:1600]
    histo = cv2.calcHist([framee],[0],None,[256],[0,256])
    bak=[]
    for j in range (0,len(histo)):
        bak.append(histo[j][0].astype(int))
    test=[]
    test.append(bak)
    eve=""
    max_score=-9999999999999999
    for j in range (0,event_count):
        reload=joblib.load(events[j]+".pkl")
        var=reload.score(test)
        if (var>max_score):
            max_score=var
            eve=events[j]
    framee = framee[(235):900, 400:1600]
    histo = cv2.calcHist([framee],[0],None,[256],[0,256])
    bak=[]
    for j in range (0,len(histo)):
        bak.append(histo[j][0].astype(int))
    test.append(bak)
    for j in range (0,event_count):
        reload=joblib.load(events[j]+".pkl")
        var=reload.score(test)
        if (var>max_score):
            max_score=var
            eve=events[j]
    
    print(eve)

'''
X=[]
lengths=[]
train_count=7
for i in range (1,train_count+1):
    name=fname+"/"+str(i)+".mp4"
    cap = cv2.VideoCapture(name)
    frameCount = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    x=0
    Xx=[]
    while (x)<frameCount:
        cap.set(1,x)
        res,frame=cap.read()
        frame = frame[(235):900, 400:1600]
        histo = cv2.calcHist([frame],[0],None,[256],[0,256])
        bak=[]
        for j in range (0,len(histo)):
            bak.append(histo[j][0].astype(int))
        Xx.append(np.array(bak))
        x=x+1
    X.append(Xx)
sample=[]
for i in range (0,len(X)):
    sample.append(np.array(X[i]))
train=np.concatenate(sample)
lengths=[]
for i in range (0,len(sample)):
    lengths.append(len(sample[i]))
lengths=np.array(lengths)

param=set(train.ravel())
model=hmm.GaussianHMM(n_components=6, covariance_type="full", n_iter=100,params=param).fit(train,lengths)
remodel=hmm.GaussianHMM(n_components=6).fit(train, lengths)
joblib.dump(model,fname+"p.pkl")
'''



