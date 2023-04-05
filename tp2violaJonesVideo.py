import cv2

# 加载级联分类器
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# 视频画面
cap = cv2.VideoCapture('video1.mp4')

fps=cap.get(cv2.CAP_PROP_FPS)
print(fps)

while True:
    # 读取视频帧
    ret, frame = cap.read()
    if not ret:
        break

    # 将视频帧转换为灰度图像
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 在灰度图像中检测人脸
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # 在视频帧上绘制矩形
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # 显示结果
    cv2.imshow('frame', frame)
    if cv2.waitKey(int(1000/fps)) == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()