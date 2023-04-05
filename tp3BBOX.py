import cv2

# 加载图片
img = cv2.imread('D:\WorkFiles\objets.bmp')
# 将图片转化为灰度图
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 进行 Canny 边缘检测
canny = cv2.Canny(gray, 30, 150)

# 进行形态学操作，使得物体区域更加连通
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
dilate = cv2.dilate(canny, kernel)

# 查找轮廓
contours, hierarchy = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 绘制矩形框
for i in range(len(contours)):
    # 获取矩形框的左上角和右下角坐标
    x, y, w, h = cv2.boundingRect(contours[i])
    # 绘制矩形框
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# 显示结果
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
