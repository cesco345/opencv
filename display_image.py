from PIL import Image
from numpy import *
from pylab import *

import cv2

# windows to display image
cv2.namedWindow("Image")



# read image
image = cv2.imread('/home/cesco/Desktop/images/logo_steve.png')
h,w = image.shape[:2]
print h,w

# save image
cv2.imwrite('/home/cesco/Desktop/images/­result.png',image)

# show image
cv2.imshow("Image", image)

# exit at closing of window
cv2.waitKey(0)
cv2.destroyAllWindows()
