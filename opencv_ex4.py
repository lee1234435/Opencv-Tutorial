import cv2
import numpy as np
import matplotlib.pyplot as plt

img_test = cv2.imread('opencv.jpg')

#OpenCV 이미지를 Matplotlib이 인식하는 RGB 형식으로 변환
img_test_rgb = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)

#yticks를 0부터 시작하도록 수정

ytick1 = np.arange(0, 500,100)
ylabel1 = ['0', '100', '200','300','400']
plt.yticks(ytick1,ylabel1[::-1])
plt.imshow(img_test)
plt.show()