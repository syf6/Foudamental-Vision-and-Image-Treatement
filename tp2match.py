import cv2
import numpy as np

# 读取图像
people = cv2.imread('image.jpg')
template = cv2.imread('template.png')

# 创建SURF检测器
# sift = cv2.xfeatures2d.SIFT_create()
sift = cv2.SIFT_create()

# points interet
keypoints = sift.detect(template,None)

# 绘制points interet
template_with_keypoints = cv2.drawKeypoints(template, keypoints, None, color=(0, 255, 0), flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow('template_with_keypoints',template_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
