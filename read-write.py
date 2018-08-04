import cv2

img = cv2.imread('subject.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imwrite('gray-subject.jpg', gray)