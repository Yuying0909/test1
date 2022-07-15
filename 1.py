import numpy as np
import cv2 as cv


x,y=np.meshgrid(np.arange(10),np.arange(8))
c=np.zeros((x.shape[0],x.shape[1],3))
c[:,:,0]=x
c[:, :, 1] = y
c[::2, ::2, 2] = 3
cv.imwrite(r'/Users/yuying/Desktop/YY/PythonProject/test/2.jpg',
           np.stack([np.uint8(c[:, :, 0] * 10), np.uint8(c[:, :, 1] * 10), np.uint8(c[:, :, 2] * 255)], axis=-1))
