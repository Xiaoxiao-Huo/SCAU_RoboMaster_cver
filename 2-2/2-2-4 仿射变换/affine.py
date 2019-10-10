'''''''''''''''''''''''''''''''''
仿射变换
Created by Xiaoxiao
2019.10.10
'''''''''''''''''''''''''''''''''

import cv2
import numpy as np
img = cv2.imread("1.jpg",1)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]

matRotate = cv2.getRotationMatrix2D((height*0.5,width*0.5),45,0.5)
# 1 center 2 angle 3 scale(缩放系数，如果不缩放即系数为1可能看不到完整图片)
rotate = cv2.warpAffine(img,matRotate,(height,width))
cv2.imshow('rotate',rotate)

#仿射变换需要将原图3个点映射到目标图片的3个点上
#3个点：左上角，左下角，右上角
matRot = np.float32([[0,0],[0,height-1],[width-1,0]])
matDst = np.float32([[height * 0.2, width * 0.1], [height * 0.9, width * 0.2], [height * 0.1, width * 0.9]])
#组合
matAffine = cv2.getAffineTransform(matRot,matDst)
#仿射变换 1 src 2 dst 得到一个矩阵
dst = cv2.warpAffine(rotate,matAffine,(width,height))
# 1 输入矩阵 2 变换矩阵 3 宽高信息
cv2.imshow('dst',dst)
cv2.waitKey(0)