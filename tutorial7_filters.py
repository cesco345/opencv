filters.py

from PIL import Image
from numpy import *
from pylab import *

import cv

image = cv.LoadImage('miches.jpg',cv.CV_LOAD_IMA­GE_GRAYSCALE)

# create the window
cv.NamedWindow('Miches', cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage('Miches', image) # show the image
cv.WaitKey() # close window


# Sobel operator
sobel = cv.CreateMat(image.height, image.width, cv.CV_32FC1)
cv.Sobel(image,sobel,1,1,3)
cv.ShowImage('Miches Sobel', sobel)
cv.SaveImage('miches_sobel.jpg', sobel)
cv.WaitKey()
________________________________________­___________________________

blur_smooth.py

from PIL import Image
from numpy import *
from pylab import *

import cv


# this will load and show an image in gray scale
image = cv.LoadImage('miches.jpg',cv.CV_LOAD_IMA­GE_GRAYSCALE)

# original image during smoothing and subtraction
blur_image = cv.CreateImage(cv.GetSize(image), image.depth, image.nChannels)


# the original image during filtering
cv.Smooth(image, blur_image, cv.CV_BLUR, 15, 15)
fil = cv.CreateImage(cv.GetSize(image), image.depth, image.nChannels)


# subtraction of the original minus the filtered one
cv.AbsDiff(image,blur_image,fil)
cv.ShowImage('Image', fil)
cv.WaitKey()
cv.SaveImage('result_image.jpg', fil)
________________________________________­______________________________



from PIL import Image
from numpy import *
from pylab import *

import cv

im = cv.LoadImageM("miches.jpg", 1)
dst = cv.CreateImage(cv.GetSize(im), cv.IPL_DEPTH_16S, 3)
laplace = cv.Laplace(im, dst)
cv.SaveImage("miches_laplace.png", dst)
