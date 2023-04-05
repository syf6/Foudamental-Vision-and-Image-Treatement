import cv2
import numpy as np

# 循环读取每个图像并显示
for i in range(1013, 1260):
    name = 'image'+str(i)+'.jpg'
    image = cv2.imread('.\\images\\'+name)

    # 显示图像并等待 25 毫秒
    cv2.imshow('frame', image)
    cv2.waitKey(25)

    # 按下 q 键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放窗口资源
cv2.destroyAllWindows()


