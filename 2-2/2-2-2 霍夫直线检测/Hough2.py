'''''''''''''''''''''''''''''''''
霍夫直线检测
Created by Xiaoxiao
2019.10.10
'''''''''''''''''''''''''''''''''

import cv2
import numpy as np

img = cv2.imread('1.jpg',1)
cv2.imshow("src",img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(3,3),0)
edge = cv2.Canny(blur,50,150)

# 霍夫直线检测
lines = cv2.HoughLinesP(edge, 0.9, np.pi/180, 90, minLineLength=30, maxLineGap=5)
# 1 canny边缘检测后图像 2 3 步长半径和角度 4 阈值 5 线的最短长度 6 线的最大间隔
for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2, lineType = cv2.LINE_AA)

cv2.imshow('HoughLinesP',img)
cv2.waitKey(0)