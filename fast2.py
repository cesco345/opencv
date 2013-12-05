import numpy as np
from matplotlib import pyplot as plt
import cv2
import scipy.fftpack 


# images imput
img1 = cv2.imread('robVanPettenPhoto.png',0)
img2 = cv2.imread('robVanPetten2.png',0)
img3 = cv2.imread('cliffMautner.png',0)
img4 = cv2.imread('bibliotequeHotelDeVille.png',0)
img5 = cv2.imread('mugaMiyahara.png',0)
img6 = cv2.imread('shinichiSato.png',0)




# Images Input, layout, and transforms
img_input = [img1, img2, img3, img4, img5, img6]
picture_name = ['Rob Van Petten', 'Rob Van Petten','Cliff Mautner', 'Benjamin Antony Monn', \
                'Muga Miyahara', 'Shinichi Sato']
fft_images = [scipy.fftpack.ifft(x) for x in img_input]
fft_shift = [scipy.fftpack.fftfreq(y) for y in fft_images]
magnitude = [np.log(np.abs(z)+1) for z in fft_shift]

for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(magnitude[i],cmap = 'gray')
    plt.title(picture_name[i]), plt.xticks([]), plt.yticks([])

plt.show()


