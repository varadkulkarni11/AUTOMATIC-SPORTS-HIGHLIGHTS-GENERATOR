import cv2 
from matplotlib import pyplot as plt
import numpy as np

img = cv2.imread('scorecard.png',1)
#hue histogram of main scorecard
hist_score = cv2.calcHist([img],[0],None,[256],[0,256]) 
c=0
vid=cv2.VideoCapture('match.mp4')
f=open('histogram_frame_numbers.txt','w')
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
        f.write(c+'\n')
    c+=1
    #cv2.imshow('window_frame',crop_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
f.close()
