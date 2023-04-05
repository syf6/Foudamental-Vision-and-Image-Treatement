import cv2
import numpy as np

# 加载图像
people = cv2.imread('image.jpg')
template = cv2.imread('template.png')

# 计算相关分数
result = cv2.matchTemplate(people, template, cv2.TM_CCOEFF)

# 显示相关分数结果图像
cv2.imshow('Result', result)

# 找到最佳分数位置
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

# 在脸部周围绘制矩形
top_left = max_loc
bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
cv2.rectangle(people, top_left, bottom_right, 255, 2)

# 显示结果图像
cv2.imshow('Group with Face Detection', people)
cv2.waitKey(0)
cv2.destroyAllWindows()
