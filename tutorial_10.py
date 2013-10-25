from PIL import Image
from numpy import *
from pylab import *

import urllib
import cv2


url = 'http://vis-www.cs.umass.edu/lfw/images/Bob_Bowlsby/Bob_Bowlsby_0001.jpg'
urllib.urlretrieve(url,'filename.png')

# windows to display image
cv2.namedWindow("Image")
image = cv2.imread('filename.png')

h,w = image.shape[:2]
print h,w

# show image
cv2.imshow("Image", image)

# save image
cv2.imwrite('/home/cesco/Desktop/images/retrieve_result.png',image)



# exit at closing of window
cv2.waitKey(0)
cv2.destroyAllWindows()
