import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    hsv1 = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    color = cv2.cvtColor(hsv1, cv2.COLOR_HSV2RGB)
    cv2.imshow('RGB Video',color)

    gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)
    cv2.imshow('Gray Video', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindolsws()