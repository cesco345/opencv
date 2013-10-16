yellow_rose.py

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


___________________________________________________________________________


resized_yellow.py

from PIL import Image
from numpy import *
from pylab import *

import cv

original = cv.LoadImageM("yellow_rose.jpg")
print type(original)
cv.NamedWindow("Resized", cv.CV_WINDOW_AUTOSIZE )
resized = cv.CreateMat(original.rows / 10, original.cols / 10, cv.CV_8UC3)
cv.Resize(original, resized)
cv.ShowImage("Resized", resized)
cv.WaitKey(10000)
cv.SaveImage("resized_yellow_rose.png", resized)
cv.DestroyWindow("Resized")
