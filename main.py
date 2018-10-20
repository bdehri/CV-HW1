import cv2
import numpy as np
import matplotlib.pyplot as plt


def histogram(i):
    R, C, B = i.shape
    hist = np.zeros((256,1,B),dtype=np.uint8)

    for g in range(256):
        hist[g, 0, ...] = np.sum(np.sum(i == g, 0), 0)

    return hist


def probdensityfunc(histogram, shape):
    probdensity = np.zeros((256, 1, 3), dtype=np.uint8)
    probdensity = histogram / shape
    return probdensity


histogram1 = np.zeros((256, 1, 3), dtype=np.uint8)
histogram2 = np.zeros((256, 1, 3), dtype=np.uint8)
probDensity1 = np.zeros((256, 1, 3), dtype=np.float32)
probDensity2 = np.zeros((256, 1, 3), dtype=np.float32)
cdf = np.zeros((256,1,1),dtype=np.uint8)

x_pos = [i for i in range(256)]

img = cv2.imread("color1.png", cv2.IMREAD_COLOR)
img2 = cv2.imread("color2.png", cv2.IMREAD_COLOR)
imgShape = img.shape[0] * img.shape[1]

histogram1 = histogram(img)
histogram2 = histogram(img2)

probDensity1 = probdensityfunc(histogram1, imgShape)
probDensity2 = probdensityfunc(histogram2, imgShape)


print(probDensity1)
print(probDensity2)

plt.bar(x_pos, histogram1[..., 0, 1])
plt.title("hist")
plt.show()

plt.bar(x_pos, probDensity1[..., 0, 1])
plt.title("probdens")
plt.show()




cv2.imshow('img', img2)

if cv2.waitKey(0)&0xFF == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif cv2.waitKey(0)&0xFF == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('color1.png', img)
    cv2.destroyAllWindows()
