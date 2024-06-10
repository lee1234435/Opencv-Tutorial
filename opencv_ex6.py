import cv2
import numpy as np


cap = cv2.VideoCapture("pexels_videos_1918465 (2160p).mp4")

while cap.isOpened():
    ret,frame = cap.read() # ret 성공 여부 , frame 받아온 이미지
    if not ret:
        print("no frames")
        break
    cv2.imshow('video',frame)
   
    if cv2.waitKey(3) == ord('q'):
        print('종료')
        break
    
cap.release()
cv2.destroyAllWindows()