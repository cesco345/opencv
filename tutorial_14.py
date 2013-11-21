from pylab import *
from numpy import *
from scipy.ndimage import filters
import harris
import cv2
from PIL import Image
import harris_run



im = array(Image.open('lady_in_red_big.jpg').convert('L'))
harrisim = harris.compute_harris_response(im)
filtered_coords = harris.get_harris_points(harrisim,6)
harris.plot_harris_points(im, filtered_coords)


