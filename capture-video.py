import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    hsv1 = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    h, s, v = cv2.split(hsv1)
    hsv2 = cv2.merge((h, s, v))
    color = cv2.cvtColor(hsv2, cv2.COLOR_HSV2RGB)
    cv2.imshow('RGB Video',color)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray Video', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindolsws()