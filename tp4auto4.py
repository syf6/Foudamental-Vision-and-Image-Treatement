import cv2
import numpy as np
# answer version
# Définir les plages de couleurs HSV pour le blanc et le jaune
lower_yellow = np.array([18, 94, 140])
upper_yellow = np.array([48, 255, 255])
lower_white = np.array([0, 0, 200])
upper_white = np.array([180, 15, 255])

# 设置感兴趣的区域
roi_vertices = np.array([[ (0,0), (1280,0),(1280,720), (700,420), (500, 420), (0, 720)]], dtype=np.int32)

for i in range(1013, 1260):
    name = 'image'+str(i)+'.jpg'
    image = cv2.imread('.\\images\\'+name)

    # 显示图像并等待 25 毫秒
    cv2.imshow('frame', image)
    cv2.waitKey(25)

    # 转换
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 创建一个黄色掩码
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # 创造一个白色掩码
    white_mask = cv2.inRange(hsv, lower_white, upper_white)

    # 合并掩码
    mask = cv2.bitwise_or(yellow_mask, white_mask)

    # 应用掩码
    result = cv2.bitwise_and(image, image, mask=mask)

    # 对结果进行边缘检测
    edges = cv2.Canny(result, 50, 150)

    # 进行扩张
    kernel = np.ones((9, 9), dtype=np.uint8)
    dilated = cv2.dilate(edges, kernel, iterations=1)

    # 选择感兴趣的区域
    masked_edges = cv2.fillPoly(dilated, roi_vertices, (0, 0, 0))

    # 应用霍夫变换
    lines = cv2.HoughLinesP(masked_edges, rho=2, theta=np.pi / 180, threshold=100, minLineLength=50, maxLineGap=100)

    # 在原始图像上绘制检测到的线条
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), thickness=2)

    # 显示图像
    cv2.imshow('detected lines', image)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# 释放窗口资源
cv2.destroyAllWindows()
