import cv2
import matplotlib.pyplot as plt

img = cv2.imread('subject.jpg')
b,g,r = cv2.split(img)

plt.subplot(121);plt.imshow(img) # expects distorted color
cv2.imshow('rgb image',img) # expects distorted color
cv2.waitKey(0)
cv2.destroyAllWindows()
