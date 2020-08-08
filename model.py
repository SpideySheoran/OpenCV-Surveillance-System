#import libraries
import cv2
import numpy as np

#initialise classifier
body_classifier = cv2.CascadeClassifier('haarcascade_upperbody.xml')

#read video
cap = cv2.VideoCapture('footage.mp4')


#model
while(cap.isOpened()):
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    bodies = body_classifier.detectMultiScale(frame, 1.5, 1)

    for (x,y,w,h) in bodies:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (25,125,255), 2)
        print(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000)
    cv2.imshow('Pedestrians', frame)
    
    
    
    if cv2.waitKey(1) == 27:
        break
    
cap.release()
cv2.destroyAllWindows()