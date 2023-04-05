import cv2
import numpy as np

# 读取图像并将其转换为灰度图像
img = cv2.imread('D:\WorkFiles\objets.bmp')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 对图像进行形态学操作，填充空洞
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
filled = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)

# 通过二值化处理进行分割
ret, thresh = cv2.threshold(filled, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# 查找轮廓
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 随机生成颜色列表，用于绘制每个轮廓
colors = np.random.randint(0, 255, size=(len(contours), 3), dtype=np.uint8)

# 绘制每个轮廓
for i in range(len(contours)):
    cv2.drawContours(img, contours, i, (int(colors[i][0]), int(colors[i][1]), int(colors[i][2])), thickness=-1)

# 显示结果
cv2.imshow('result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
