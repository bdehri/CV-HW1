import cv2
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline


def histogram(i):
    R, C, B = i.shape
    hist = np.zeros((256,1,B),dtype=np.uint8)

    for g in range(256):
        hist[g, 0, ...] = np.sum(np.sum(i == g, 0), 0)

    return hist


histogram1 = np.zeros((256, 1, 3), dtype=np.uint8)
histogram2 = np.zeros((256, 1, 3), dtype=np.uint8)


img = cv2.imread("color1.png")
img2 = cv2.imread("color2.png")

histogram1 = histogram(img)
histogram2 = histogram(img2)
print(img.shape)
print(img2.shape)
print(histogram1.shape)
print(histogram2.shape)

plt.bar(histogram1[...,0,0])


cv2.imshow('img', img2)

if cv2.waitKey(0)&0xFF == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif cv2.waitKey(0)&0xFF == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('color1.jpeg', img)
    cv2.destroyAllWindows()
