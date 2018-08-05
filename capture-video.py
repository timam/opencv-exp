import numpy as np
import cv2

cap = cv2.VideoCapture(0)


def make_480p():
    cap.set(3, 640)
    cap.set(4, 480)

make_480p()

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)


while(True):
    ret, frame = cap.read()

    frame50 = rescale_frame(frame, percent=50)
    frame25 = rescale_frame(frame, percent=25)

    hsv1 = cv2.cvtColor(frame50, cv2.COLOR_RGB2HSV)
    color = cv2.cvtColor(hsv1, cv2.COLOR_HSV2RGB)
    cv2.imshow('RGB Video',color)

    gray = cv2.cvtColor(frame25, cv2.COLOR_RGB2GRAY)
    cv2.imshow('Gray Video', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindolsws()