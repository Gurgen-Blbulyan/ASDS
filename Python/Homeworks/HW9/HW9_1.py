import numpy as numpy
import cv2 as cv



img = cv.imread('pic1.jpg')
cv.imshow('pic1', img)

img = cv.imread('pic2.jpg')
cv.imshow('pic2', img)

img = cv.imread('pic3.jpg')
cv.imshow('pic3', img)


cv.waitKey(0)	

