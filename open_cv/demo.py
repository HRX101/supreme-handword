import cv2 
import csv
import subprocess
from cvzone.FaceDetectionModule import FaceDetector
from cvzone.HandTrackingModule import HandDetector
from cvzone import *
from cv2 import data
import cvzone
import time
from tkinter import *
from cvzone import *
vid=cv2.VideoCapture(0)
detector=HandDetector(detectionCon=0.8)
face_detector=FaceDetector(minDetectionCon=0.5)
while True:
    frame,image=vid.read()
    image=cv2.flip(image,1)
    hands,image=detector.findHands(image,flipType=False)
    if hands:
        lm=hands[0]['lmList']
        dis,info=detector.findDistance(lm[8],lm[12])
        dis1,info1=detector.findDistance(lm[8],lm[20])
        bye_dis,info2,image=detector.findDistance(lm[4],lm[8],image)
        if(dis>60 and dis<70):
            subprocess.Popen('C:\\Windows\\System32\\write.exe')
        elif(dis1>80 and dis1<90):
            subprocess.Popen("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe")
        elif (bye_dis>100 and bye_dis<120):
            break
        else:
            print("not")
    cv2.imshow("demo",image)
    if cv2.waitKey(1)==ord('a'):
        break
vid.release()
cv2.destroyAllWindows()
