import cv2
import numpy as np
import keras

from threading import Timer
import datetime
import os
def exitfunc():
    print("Completed Taking pictures")
    os._exit(0)

def draw_Rounded_Corners(img, pt1, pt2, color, thickness, r, d):
    x1,y1 = pt1
    x2,y2 = pt2

    # Top left
    cv2.line(img, (x1 + r, y1), (x1 + r + d, y1), color, thickness)
    cv2.line(img, (x1, y1 + r), (x1, y1 + r + d), color, thickness)
    cv2.ellipse(img, (x1 + r, y1 + r), (r, r), 180, 0, 90, color, thickness)

    # Top right
    cv2.line(img, (x2 - r, y1), (x2 - r - d, y1), color, thickness)
    cv2.line(img, (x2, y1 + r), (x2, y1 + r + d), color, thickness)
    cv2.ellipse(img, (x2 - r, y1 + r), (r, r), 270, 0, 90, color, thickness)

    # Bottom left
    cv2.line(img, (x1 + r, y2), (x1 + r + d, y2), color, thickness)
    cv2.line(img, (x1, y2 - r), (x1, y2 - r - d), color, thickness)
    cv2.ellipse(img, (x1 + r, y2 - r), (r, r), 90, 0, 90, color, thickness)

    # Bottom right
    cv2.line(img, (x2 - r, y2), (x2 - r - d, y2), color, thickness)
    cv2.line(img, (x2, y2 - r), (x2, y2 - r - d), color, thickness)
    cv2.ellipse(img, (x2 - r, y2 - r), (r, r), 0, 0, 90, color, thickness)


print("Please enter your name >")
#take user name as input to create a directory on person name
SubDirectoryName = str(input())

#path for parent directory
Parent = "C:/Users/Hameed/Documents/GitHub/Flames/note4/Persons-Name-Identification-using-python-opencv"
  
# Path for subdirectory
path = os.path.join(Parent, SubDirectoryName) 
os.mkdir(path)
import time
c=15
# timer='00:00'
# while c:
        # mins, secs, = divmod(15, 60)
       # c -= 1
        # time.sleep(1)
        # timer='00:{:02d}'.format(c)
         
#Timer(15, exitfunc).start()

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
c=15
time_start = time.time()
print(time_start)
timer_endtime=int(time.time() - time_start)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
VideoFileName=SubDirectoryName+'.avi'
out = cv2.VideoWriter(VideoFileName,fourcc, 20.0, (640,480))

while True:
        Timer(15, exitfunc).start()
        ret, frame = cap.read()
        out.write(frame)
        if not ret:
            break
        facecasc = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = facecasc.detectMultiScale(gray,scaleFactor=1.3, minNeighbors=5)
        canvas = np.zeros((250, 300, 3), dtype="uint8")
        for (x, y, w, h) in faces:
            draw_Rounded_Corners(frame, (x, y-50), (x+w, y+h+10), (255, 0, 0), 2,15, 10) 
            roi_gray = gray[y:y + h, x:x + w]
            cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)

        
        timer_endtime=c-int(time.time() - time_start)
        timer='00:{:02d}'.format(timer_endtime)
        cv2.putText(frame,timer , (260,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
               
        cv2.imshow('Add photos', cv2.resize(frame,(640,480),interpolation = cv2.INTER_CUBIC))
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
             break
      
cap.release()
out.release()


cv2.destroyAllWindows()
