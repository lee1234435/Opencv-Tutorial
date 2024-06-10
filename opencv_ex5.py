import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while (cap.isOpened()):
    ret,img = cap.read()
    cv2.imshow('my face',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print(ret,img)
cap.release()
cv2.destroyAllWindows()

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,240)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
writer = cv2.VideoWriter('video.avi',fourcc,25.0,(320,240))
while (cap.isOpened()):
    ret,img = cap.read()
    cv2.imshow('my face',img)
    writer.write(img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release() # 작동 시키고 난 후 종료시 해제를 하기 위함
writer.release()
cv2.destroyAllWindows()