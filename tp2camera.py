import cv2

# 加载模板
template = cv2.imread('template2.jpg', cv2.IMREAD_GRAYSCALE)

# 获取模板大小
w, h = template.shape[::-1]

# 定义相关分数计算方法
method = cv2.TM_CCORR

# 捕获电脑摄像头的实时画面
cap = cv2.VideoCapture(0)

while True:
    # 读取视频帧
    ret, frame = cap.read()
    if not ret:
        break

    # 将视频帧转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 计算相关分数
    res = cv2.matchTemplate(gray, template, method)

    # 获取最佳分数和对应的位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # 在视频帧上绘制矩形
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 2)

    # 显示结果 
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
