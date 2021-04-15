import cv2
import numpy as np

def perspective_transform(x1,x2,x3,x4,x5,x6,x7,x8,x9,img):
    M=np.matrix([[x1,x2,x3],[x4,x5,x6],[x7,x8,x9]])
    img = cv2.warpPerspective(img,M,(512,512))
    return img