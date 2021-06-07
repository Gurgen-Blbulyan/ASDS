import cv2 as cv
import numpy as np

img = cv.imread('pic2.jpg') 

cv.imshow('pic2', img) 

average = cv.blur(img, (7,7))

cv.imshow('average blur', average)

bilateral1 = cv.bilateralFilter(img, 30,100, 40)  #img, diameter, sigmacolor (larger value means more colors in the neighbourhood will be considered when the blur is computed), sigmaSpace (larger values means that pixels further out of the center pixel will influence the bluring calculation)

cv.imshow('bilateral', bilateral1)


cv.waitKey(0)

# we can see that in bilateral methodethe edges of the image are retained