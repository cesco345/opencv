import requests
import cv

r = requests.get('http://www.autoshowup.com/stockimg/gable-of-a-half-timbered-house-in-black-and-white-in-a-traditional-german-village.jpg')
with open('imported_pic.jpg','wb') as f:
   f.write(r.content)

#r = requests.get('http://www.free-macrame-patterns.com/image-files/diamond-stitch-medium.jpg')
#with open('imported_pic.jpg','wb') as f:
#   f.write(r.content)

#imcolor = cv.LoadImage('lady_in_red_big.jpg')
#image = cv.LoadImage('lady_in_red_big.jpg',cv.CV_LOAD_IMAGE_GRAYSCALE)


imcolor = cv.LoadImage('imported_pic.jpg')
image = cv.LoadImage('imported_pic.jpg',cv.CV_LOAD_IMAGE_GRAYSCALE)
cornerMap = cv.CreateMat(image.height, image.width, cv.CV_32FC1)



# OpenCV corner detection
cv.CornerHarris(image,cornerMap,3)

for y in range(0, image.height):
    for x in range(0, image.width):
        harris = cv.Get2D(cornerMap, y, x) # get the x,y value

  # check the corner detector response
        if harris[0] > 10e-06:
    # draw a small circle on the original image
            cv.Circle(imcolor,(x,y),1,cv.RGB(35, 0,165))

cv.NamedWindow('Harris Corner Image', cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage('Harris Corner Image', imcolor) # show the image
cv.SaveImage('harris_corner_image.jpg', imcolor)
cv.WaitKey()

