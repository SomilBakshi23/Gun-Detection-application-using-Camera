import numpy as np
import cv2
import imutils

gun_cascade = cv2.CascadeClassifier('cascade.xml')
camera = cv2.VideoCapture(0)

firstFrame = None
gun_exist = False

while True:
    ret, frame = camera.read()
    
    if not ret or frame is None:
        print("Failed to capture image")
        break

    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gun = gun_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(100, 100))

    if len(gun) > 0:
        gun_exist = True
    else:
        gun_exist = False

    for (x, y, w, h) in gun:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Red rectangle for gun detection

    if firstFrame is None:
        firstFrame = gray
        continue

    cv2.imshow("Security Feed", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

    if gun_exist:
        print("Gun Detected")
    else:
        print("Gun Not Detected")

camera.release()
cv2.destroyAllWindows()
