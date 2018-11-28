import cv2 
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('scorecard.png',1)
#hue histogram of main scorecard
hist_score = cv2.calcHist([img],[0],None,[256],[0,256]) 
c=0
vid=cv2.VideoCapture('match.mp4')
frames=[]
length = int(vid.get(cv2.CAP_PROP_FRAME_COUNT))
print( length )
print((vid.get(cv2.CAP_PROP_FPS)))
while True:
    ret, imag=vid.read()

    #cropping image/frame to compare only the bottom part
    crop_img = imag[(1080-135):1080, 0:1920]

    #hue histogram of current frame
    hist_cur = cv2.calcHist([crop_img],[0],None,[256],[0,256])

    #calculate histogram similarity
    mini=np.minimum(hist_cur,hist_score)
    x=np.true_divide(np.sum(mini),np.sum(hist_score))
    
    #getting frame indices
    if x>=0.65:
        frames.append(c)
    c+=1
    #cv2.imshow('window_frame',crop_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

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

