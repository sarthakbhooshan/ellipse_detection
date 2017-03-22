# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 16:51:45 2017

@author: Sarthak Bhooshan
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(1)
cap.set(5,0)

while(True):
    # Capture frame-by-frame
   
    ret, img = cap.read()
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mblur = cv2.medianBlur(imgray,5)
    equ = cv2.equalizeHist(mblur)
    ret,thresh = cv2.threshold(equ,127,255,cv2.THRESH_BINARY)
    #thresh = cv2.adaptiveThreshold(mblur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,2)
    res = cv2.medianBlur(thresh,3)
    
    
    img2,contours,hierarchy = cv2.findContours(res,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours( img, contours,-1, (128,255,255), 2)
    for cnt in contours:
        if len(cnt) > 5: # at least 5 pts needed
            
            box = cv2.fitEllipse(cnt)
            (x,y),(MA,ma),angle=cv2.fitEllipse(cnt)
            if(240>MA>100):
                cv2.ellipse(img,box,(200,0,0), 2)
                if(150>MA>50):
                    print (x,y)

    cv2.imshow('contours', mblur)
    cv2.imshow('mywindow', thresh)
    
    cv2.imshow('cont', img)
    if cv2.waitKey(1) == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()