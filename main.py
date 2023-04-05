import cv2
import numpy as np

# 读取图像
person = cv2.imread('image.jpeg')
beach = cv2.imread('plage.jpg')

redChannel = person[:, :, 2] # Red channel
greenChannel = person[:, :, 1] # Green channel
blueChannel = person[:, :, 0] # Blue channel

rws, cls = person[:, :, 0].shape

mask = np.zeros((rws, cls), dtype=np.uint8)

for i in range(rws):
    for j in range(cls):
        if redChannel[i, j] < 100 and greenChannel[i, j] < 150 and blueChannel[i, j] > 152:
            mask[i, j] = 0
            #black
        else:
            mask[i, j] = 255
            #white

only = cv2.bitwise_and(person, person, mask=mask)
#result = cv2.addWeighted(only,0.5, beach,0.5,0 )

line, col = only[:, :, 0].shape

mask2 = np.zeros((rws, cls, 3), dtype=np.uint8)

for i in range(line):
    for j in range(col):
        if only[i, j].all() == 0:
            mask2[i, j, 0] = beach[i, j, 0]
            mask2[i, j, 1] = beach[i, j, 1]
            mask2[i, j, 2] = beach[i, j, 2]
            #black
        else:
            mask2[i, j, 0] = only[i, j, 0]
            mask2[i, j, 1] = only[i, j, 1]
            mask2[i, j, 2] = only[i, j, 2]
            #white

# 显示结果
cv2.imshow('mask', mask)
cv2.imshow('only', only)
cv2.imshow('result', mask2)
cv2.waitKey(0)
cv2.destroyAllWindows()
