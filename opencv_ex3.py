import cv2
import numpy as np
import matplotlib.pyplot as plt

img_file = cv2.imread("lemon.png", cv2.IMREAD_COLOR) # 파일 읽기
cv2.imshow("lemon.png", img_file) # 파일 보여주기
key = cv2.waitKey(0)
if key == 27: # ESC
    cv2.imwrite("lemon1.png",img_file) # 이름 변경 후 저장
cv2.destroyAllWindows()

img_test = cv2.imread('opencv.jpg')
plt.imshow(img_test)
plt.show()