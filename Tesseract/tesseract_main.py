import cv2
import subprocess
import glob
from PIL import Image
import pytesseract
import numpy as np
import tempfile
import re
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *
from shutil import copyfile
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
fgbg = cv2.createBackgroundSubtractorMOG2()
def ocr(path):
    temp = tempfile.NamedTemporaryFile(delete=False)

    process = subprocess.Popen(['tesseract', path, temp.name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,shell=True)
    process.communicate()

    with open(temp.name + '.txt', 'r') as handle:
        contents = handle.read()
    return contents
def gray(image):
    grayValue = 0.07 * image[:,:,2] + 0.72 * image[:,:,1] + 0.21 * image[:,:,0]
    gray_img = grayValue.astype(np.uint8)
    return gray_img
ct=42
'''
ct=16
one=140
two=1000
three=380
four=550
dire='balls\\2inn\\*.mp4'
files=glob.glob(dire)
for filname in files:
    name=filname
    print(name)
    hl=0
    cap=cv2.VideoCapture(name)
    fc = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    god=[]
    for i in range(0,fc):
        cap.set(1,i)
        ress,frame=cap.read()
        frame = frame[(1080-one):two, three:four]
        frame=gray(frame)
        fgmask = fgbg.apply(frame)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
        cv2.imwrite('first.jpg',frame)
        strr = ocr('first.jpg')
        stri=''
        for j in range (0,len(strr)):
            if(strr[j]>='0' and strr[j]<='9' or strr[j]=='/'):
                stri+=strr[j]
        strr=stri
        if(len(strr)==0):
            continue;
        if (strr[0]>='0'and strr[0]<='9'):
            run=''
            wikt=''
            wkt=0
            for j in range(0,len(strr)):
                if(strr[j]>='0' and strr[j]<='9' and wkt==0):
                    wikt+=(strr[j])
                if(strr[j]=='/'):
                    wkt=1
                if(strr[j]>='0' and strr[j]<='9' and wkt==1):
                    run+=(strr[j])
            if (len(run)>0 and len(wikt)>0):
                god.append(((run),(wikt)))
            break
    k=-1
    if (len(god)!=0):
        k=fc-1
    while(k>=0):
        cap.set(1,k)
        k-=1
        ress,frame=cap.read()
        frame = frame[(1080-one):two, three:four]
        frame=gray(frame)
        fgmask = fgbg.apply(frame)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
        cv2.imwrite('first.jpg',frame)
        strr = ocr('first.jpg')
        stri=''
        for j in range (0,len(strr)):
            if(strr[j]>='0' and strr[j]<='9' or strr[j]=='/'):
                stri+=strr[j]
        strr=stri
        if(len(strr)==0):
            continue;
        if (strr[0]>='0'and strr[0]<='9'):
            wikt=''
            wkt=0
            run=''
            for j in range(0,len(strr)):
                if(strr[j]>='0' and strr[j]<='9' and wkt==0):
                    wikt+=(strr[j])
                if(strr[j]=='/'):
                    wkt=1
                if(strr[j]>='0' and strr[j]<='9' and wkt==1):
                    run+=(strr[j])
            if (len(run)>0 and len(wikt)>0):
                god.append(((run),(wikt)))
            break
    print(god)
    if(len(god)==0):
        hl=1
    else:
        run1,wkt1=god[0]
        run2,wkt2=god[1]
        runs=abs(int(run2)-int(run1))
        wkts=int(wkt2)-int(wkt1)
        if(runs>=4 or wkts>0):
            hl=1
    if (hl==1):
        if(len(god)!=0):
            print('HIGHLIGHT!\nRuns: '+str(runs)+'\nWkts: '+str(wkts))
        copyfile(name, 'hl clips\\'+str(ct)+'.mp4')
        ct+=1
'''


clips=[]

for i in range (0,ct):
    name="hl clips\\"+str(i+1)+".mp4"
    clips.append(VideoFileClip(name))

final_clip = concatenate_videoclips(clips)
final_clip.write_videofile("highlight.mp4")

'''
cap.set(1,fc-5)
ress,frame=cap.read()
frame = frame[(1080-one):two, three:four]
cv2.imwrite('second.jpg',frame)
command="py juggu.py first.jpg first_out.jpg"
subprocess.call(command,shell=True)
print (pytesseract.image_to_string(Image.open('first_out.jpg'),config="-c tessedit_char_whitelist=0123456789/"))
command="py juggu.py second.jpg second_out.jpg"
subprocess.call(command,shell=True)
print (pytesseract.image_to_string(Image.open('second_out.jpg'),config="-c tessedit_char_whitelist=0123456789/"))
'''
