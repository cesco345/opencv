from PIL import Image
from numpy import *
from pylab import *

import cv2

# read image
filename = '/home/cesco/Desktop/images/pic3.png'
im = cv2.imread(filename)
h,w = im.shape[:2]

# flood fill example
diff = (6,6,6)
mask = zeros((h+2,w+2),uint8)
cv2.floodFill(im,mask,(10,10), (145,255,0),diff,diff)

# show the result in an OpenCV window
cv2.imshow('Flood Fill Image',im)
cv2.waitKey(0)
cv2.destroyAllWindows()

# save the result
cv2.imwrite('/home/cesco/Desktop/images/­result.jpg',im)
