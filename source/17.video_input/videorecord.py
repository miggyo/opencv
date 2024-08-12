import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def cartoon_filter(img):
    h, w = img.shape[:2]
    img2 = cv2.resize(img, (w//2, h//2))
    blr = cv2.bilateralFilter(img2, -1, 20, 7)
    edge = 255 - cv2.Canny(img2, 80, 120)
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    edge = cv2.resize(edge, (w, h))
    dst = cv2.bitwise_and(blr, edge)
    dst = cv2.resize(dst, (w, h), interpolation=cv2.INTER_NEAREST)
    return dst

if not cap.isOpened():
    raise RuntimeError("ERROR! Unable to open camera")

try:
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    heigth= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print(f'width = {width}, height = {heigth}')

    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('./test__.avi',fourcc, 20,(width, heigth), isColor=False)

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        cartoon = cartoon_filter(gray)
        cv2.imshow('frame', cartoon)
        out.write(cartoon)

        if cv2.waitKey(1) == 27 :
            break

finally:
    cap.release()
    out.release()
    cv2.destroyAllWindows()