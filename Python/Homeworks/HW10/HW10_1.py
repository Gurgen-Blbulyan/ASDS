import cv2 as cv

img = cv.imread('pic1.jpg') 

cv.imshow('pic1', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Gray', gray)

cv.waitKey(0)