import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # For our webcam
# videoFile = cv2.VideoCapture("video.mp4") # For a video file

# Reading webcam
while True:
    ret, frame = cap.read()  # frame is an image
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == ord("A") or key == ord("a"):
        break

cap.release()  # Break capturing frames
cv2.destroyAllWindows()

