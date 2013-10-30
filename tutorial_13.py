import numpy as np
from matplotlib import pyplot as plt
from scipy import ndimage
from skimage import filter
import cv2



img = cv2.imread('lady_in_red_big.jpg',0)
im = ndimage.gaussian_filter(img, 4)
im += 0.2 * np.random.random(img.shape)

# Canny filter for two different values of sigma
edges1 = filter.canny(im)
edges2 = filter.canny(im, sigma=3)

# data display
plt.figure(figsize=(8, 3))

plt.subplot(131)
plt.imshow(im, cmap=plt.cm.jet)
plt.axis('off')
plt.title('noisy image', fontsize=20)

plt.subplot(132)
plt.imshow(edges1, cmap=plt.cm.gray)
plt.axis('off')
plt.title('Canny filter, $\sigma=1$', fontsize=20)

plt.subplot(133)
plt.imshow(edges2, cmap=plt.cm.gray)
plt.axis('off')
plt.title('Canny filter, $\sigma=3$', fontsize=20)

plt.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                    bottom=0.02, left=0.02, right=0.98)

plt.show()


# And now using OpenCV, with the above cv2 import
img = cv2.imread('lady_in_red_big.jpg',0)
edges11 = cv2.Canny(img,100,200)
edges22 = cv2.Canny(img,200,300)


plt.subplot(131)
plt.imshow(img,cmap='gray')
plt.axis('off')
plt.title('Gray Image', fontsize=20)


plt.subplot(132)
plt.imshow(edges11,cmap = 'gray')
plt.axis('off')
plt.title('Lower MinVal', fontsize=20)


plt.subplot(133)
plt.imshow(edges22,cmap = 'gray')
plt.axis('off')
plt.title('Higher MinVal', fontsize=20)

plt.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9,
                    bottom=0.02, left=0.02, right=0.98)
plt.show()

