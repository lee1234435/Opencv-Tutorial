import cv2
import numpy as np


img_file = cv2.imread("lemon.png",cv2.IMREAD_UNCHANGED)
cv2.imshow('image',img_file)
cv2.waitKey(0)

a = np.zeros((2,5), np.uint8)
b = np.ones((3,1), np.uint8)
c = np.empty((1,5), np.float32)
d = np.full((5,15), np.float32)

print(a.shape, b.shape, c.shape, d.shape)
print(a)
print(b)
print(c)
print(d)