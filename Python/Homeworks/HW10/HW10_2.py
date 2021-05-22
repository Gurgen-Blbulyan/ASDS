import cv2 as cv

img = cv.imread('pic1.jpg') 

cv.imshow('pic1', img)

blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT) 
cv.imshow('Blur3', blur)

blur = cv.GaussianBlur(img, (11, 11), cv.BORDER_DEFAULT) 
cv.imshow('Blur11', blur)

cv.waitKey(0)
