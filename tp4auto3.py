import cv2
import numpy as np

# HSV 过滤器参数
low_yellow = np.array([18, 94, 140])
high_yellow = np.array([48, 255, 255])
low_white = np.array([0, 0, 200])
high_white = np.array([180, 15, 255])

# 感兴趣的区域
roi = np.array([[(0, 720), (0, 400), (640, 300), (1280, 400), (1280, 720)]], dtype=np.int32)

# 创建一个矩形掩码
mask = np.zeros((720, 1280), dtype=np.uint8)
cv2.fillPoly(mask, roi, 255)

# 循环读取每个图像并显示
for i in range(1013, 1260):
    name = 'image'+str(i)+'.jpg'
    image = cv2.imread('.\\images\\'+name)

    # 将图像转换为 HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 应用 HSV 过滤器并合并掩码
    yellow_mask = cv2.inRange(hsv, low_yellow, high_yellow)
    white_mask = cv2.inRange(hsv, low_white, high_white)
    mask_combined = cv2.bitwise_or(yellow_mask, white_mask)
    mask_combined = cv2.bitwise_and(mask_combined, mask)

    # 运行 Canny 边缘检测
    edges = cv2.Canny(mask_combined, 50, 150)

    # 进行扩张
    kernel = np.ones((5, 5), dtype=np.uint8)
    dilated = cv2.dilate(edges, kernel, iterations=1)

    # 寻找轮廓并过滤掉面积较小的轮廓
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    filtered_contours = []
    for c in contours:
        area = cv2.contourArea(c)
        if area > 100:
            filtered_contours.append(c)

    # 绘制轮廓
    contour_image = np.zeros_like(image)
    cv2.drawContours(contour_image, filtered_contours, -1, (0, 0, 255), 3)

    # 将轮廓添加到原始图像中
    result = cv2.addWeighted(image, 0.8, contour_image, 1, 0)

    # 显示图像并等待 25 毫秒
    cv2.imshow('result', result)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# 释放资源
cv2.destroyAllWindows()
