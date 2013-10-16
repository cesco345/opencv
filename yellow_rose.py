from PIL import Image
from numpy import *
from pylab import *

import cv

im = cv.LoadImageM("yellow_rose.jpg")
print type(im)
cv.NamedWindow("Rose", cv.CV_WINDOW_AUTOSIZE )
cv.ShowImage("New Rose", im)
cv.WaitKey(10000)
cv.SaveImage("new_yellow_rose.png", im)
cv.DestroyWindow("Rose")

