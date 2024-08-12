import cv2
import numpy as np

img = np.ones((512,512,3),np.uint8)

def draw_circle(event, x,y,flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)


cv2.namedWindow(winname='MY_FIRST_DRAWING')
cv2.setMouseCallback('MY_FIRST_DRAWING',draw_circle,img)

while True:
    cv2.imshow('my_first_drawing',img)

    if cv2.waitKey(10) == 27:
        break

cv2.destroyAllWindows()