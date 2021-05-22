import cv2 as cv
import numpy as np

img = cv.imread('pic3.jpg') 

cv.imshow('pic3', img)

canny = cv.Canny(img, 125, 175)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

blank = np.zeros(img.shape, dtype = 'uint8')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1) 
cv.imshow('contours1', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)


canny = cv.Canny(blur, 125, 175)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

blank = np.zeros(img.shape, dtype = 'uint8')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1) 
cv.imshow('contours2', blank)

cv.waitKey(0)