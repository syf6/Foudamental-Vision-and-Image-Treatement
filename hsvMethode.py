import cv2
import numpy as np

# 读取图像
person = cv2.imread('image.jpeg')
beach = cv2.imread('plage.jpg')

hsv_person = cv2.cvtColor(person, cv2.COLOR_BGR2HSV)
hsv_beach = cv2.cvtColor(beach, cv2.COLOR_BGR2HSV)

# 设定蓝色阈值
lower_blue = np.array([100, 50, 50])
upper_blue = np.array([130, 255, 255])

# 生成蓝色掩码
mask = cv2.inRange(hsv_person, lower_blue, upper_blue)

# 反转蓝色掩码
mask_inv = cv2.bitwise_not(mask)

# 将蓝色区域替换为白色
white_img = np.full(person.shape, 255, dtype=np.uint8)
res = cv2.bitwise_and(person, person, mask=mask_inv) + cv2.bitwise_and(white_img, white_img, mask=mask)

# 显示结果
cv2.imshow('original', person)
cv2.imshow('result', res)
cv2.waitKey(0)
cv2.destroyAllWindows()