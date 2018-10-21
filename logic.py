import cv2
import numpy as np
import matplotlib.pyplot as plt


def histogram(i):
    R, C, B = i.shape
    hist = np.zeros((256,1,B),dtype=np.uint32)

    for g in range(256):
        hist[g, 0, ...] = np.sum(np.sum(i == g, 0), 0)

    return hist


def probdensityfunc(histogram, shape):
    probdensity = np.zeros((256, 1, 3), dtype=np.float32)
    probdensity = histogram / shape
    return probdensity


def cumulativedistfuncrgb(probdensity):
    return np.cumsum(probdensity[..., 0, 0]), np.cumsum(probdensity[..., 0, 1]), np.cumsum(probdensity[..., 0, 2])


def createlookuptable(cdfinput,cdftarget):
    lut = np.zeros((256, 1, 3), dtype=np.float32)
    gj = np.zeros(3, dtype=np.uint32)
    for gi in range(256):
        while (cdftarget[gj[0], 0, 0] < cdfinput[gi, 0, 0]) and (gj[0] < 255):
            gj[0] = gj[0]+1
        lut[gi, 0, 0] = gj[0]

        while (cdftarget[gj[1], 0, 1] < cdfinput[gi, 0, 1]) and (gj[1] < 255):
            gj[1] = gj[1] + 1
        lut[gi, 0, 1] = gj[0]

        while (cdftarget[gj[2], 0, 2] < cdfinput[gi, 0, 2]) and (gj[2] < 255):
            gj[2] = gj[2] + 1
        lut[gi, 0, 2] = gj[2]

    return lut




histogram1 = np.zeros((256, 1, 3), dtype=np.uint32)
histogram2 = np.zeros((256, 1, 3), dtype=np.uint32)
probDensity1 = np.zeros((256, 1, 3), dtype=np.float32)
probDensity2 = np.zeros((256, 1, 3), dtype=np.float32)
cdf = np.zeros((256, 1, 3), dtype=np.float32)
cdf2 = np.zeros((256, 1, 3), dtype=np.float32)
lut = np.zeros((256, 1, 3), dtype=np.float32)

x_pos = [i for i in range(256)]

img = cv2.imread("color2.png", cv2.IMREAD_COLOR)
img2 = cv2.imread("color1.png", cv2.IMREAD_COLOR)
imgShape = img.shape[0] * img.shape[1]


histogram1 = histogram(img)
histogram2 = histogram(img2)

probDensity1 = probdensityfunc(histogram1, imgShape)
probDensity2 = probdensityfunc(histogram2, imgShape)


cdf[..., 0, 0], cdf[..., 0, 1], cdf[..., 0, 2] = cumulativedistfuncrgb(probDensity1)
cdf2[..., 0, 0], cdf2[..., 0, 1], cdf2[..., 0, 2] = cumulativedistfuncrgb(probDensity2)

lut = createlookuptable(cdf, cdf2)

print(lut)

plt.bar(x_pos, histogram1[..., 0, 1])
plt.title("hist")
plt.show()

plt.bar(x_pos, probDensity1[..., 0, 1])
plt.title("probdens")
plt.show()

for i in range(img.shape[0]):
    for y in range(img.shape[1]):
        img[i, y, 0] = lut[img[i, y, 0], 0, 0]
        img[i, y, 1] = lut[img[i, y, 1], 0, 1]
        img[i, y, 2] = lut[img[i, y, 2], 0, 2]
print(img)
cv2.imshow('img', img)

if cv2.waitKey(0)&0xFF == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif cv2.waitKey(0)&0xFF == ord('s'):  # wait for 's' key to save and exit
    cv2.imwrite('color1.png', img)
    cv2.destroyAllWindows()
