import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)

img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = np.zeros((512,512,3),np.uint8)


pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
img = cv2.polylines(img,[pts],True,(0,255,255))

pts = pts.reshape((-1,1,2))
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

