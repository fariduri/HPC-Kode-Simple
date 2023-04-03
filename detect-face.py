import numpy as np
import cv2 as cv

# 1301180513

cap = cv.VideoCapture(0)
faceCascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
eyeCascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_eye.xml")

print("press 'q' to exit")
while True:
    ret, frame = cap.read()

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 4)
        
        roiGray = gray[y:y+h, x:x+w]
        roiColor = frame[y:y+h, x:x+w]
        eyes = eyeCascade.detectMultiScale(roiGray, 1.3, 5)

        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roiColor, (ex, ey), (ex+ew, ey+eh), (0, 200, 200), 4)

    cv.imshow('Web Cam', frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
