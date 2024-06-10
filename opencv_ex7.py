import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

for i in range(0,101,1):
    # if i <= 100:
        img = cv2.line(img,(0,0),(i,i),(255,0,0),5)
        
for i in range(101,301,1):
    # if i > 100 & i <= 300:
        img = cv2.line(img,(101,101),(i,i),(0,255,0),5)
        
for i in range(301,513,1):       
    # if i > 300 & i <= 512:
        img = cv2.line(img,(301,301),(i,i),(0,0,255),5)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()