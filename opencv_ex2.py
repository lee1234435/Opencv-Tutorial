import cv2
import numpy as np

img_file = cv2.imread("lemon.png",cv2.IMREAD_UNCHANGED)
img_file1 = cv2.imread("lemon.png",cv2.IMREAD_REDUCED_COLOR_4)
img_gray = cv2.imread("lemon.png",cv2.IMREAD_GRAYSCALE)
img_gray1 = cv2.imread("lemon.png",cv2.IMREAD_REDUCED_GRAYSCALE_4)

cv2.imshow('color',img_file)
cv2.imshow('color1',img_file1)
cv2.imshow('gray', img_gray)
cv2.imshow('gray1', img_gray1)

a = img_file1.shape # 튜플 형태, 높이 넓이 채널 순서로 값이 나옴
print(a)

cv2.waitKey(0) #어떤 키가 눌러질때 까지 무한 대기
cv2.destroyAllWindows() #키눌러졌을때 전부 종료