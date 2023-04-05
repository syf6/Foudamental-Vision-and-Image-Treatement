import cv2
import numpy as np

I = cv2.imread('D:\WorkFiles\objets.bmp', cv2.IMREAD_GRAYSCALE)

SE = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))

I[I > 115] = 255
I[I < 115] = 0

# dilat - erode
O = cv2.morphologyEx(I, cv2.MORPH_OPEN, SE)
C = cv2.morphologyEx(O, cv2.MORPH_CLOSE, SE)

I2 = cv2.Canny(C, 0, 1)

J = cv2.copyMakeBorder(I2, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=0)
J = cv2.bitwise_not(J)
cv2.floodFill(J, None, (0, 0), 255)
J = cv2.bitwise_not(J)

# Resize I2 to match the size of J
I2 = cv2.resize(I2, (J.shape[1], J.shape[0]))

J = cv2.bitwise_and(J, I2)

cv2.imshow("I2", I2)
cv2.imshow("J", J)
cv2.waitKey(0)
cv2.destroyAllWindows()
