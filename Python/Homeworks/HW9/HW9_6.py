import cv2 as cv

img = cv.imread('pic2.jpg')
img1 = cv.imread('pic2.jpg')

cv.rectangle(img, (20,100), 
             (50,50),
             (0, 69, 255), thickness = 2)

cv.imshow('Original', img1)
cv.imshow('Rectangle', img)


cv.waitKey(0)