import cv2
import numpy as np

# rgb_color = np.uint8([[[0,255,0]]])
# rgb_color = np.uint8([[[40,40,40]]])
rgb_color = np.uint8([[[0, 255, 0]]])
hsv_color = cv2.cvtColor(rgb_color,cv2.COLOR_BGR2HSV)
print(hsv_color)
