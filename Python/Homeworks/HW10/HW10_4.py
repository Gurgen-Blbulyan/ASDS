import cv2 as cv

img = cv.imread('pic2.jpg') 

cv.imshow('pic2', img)

resize = cv.resize(img, (img.shape[1]*2, img.shape[0]), interpolation = cv.INTER_LINEAR) 
cv.imshow('Resize1', resize)

resize = cv.resize(img, (img.shape[1], int(img.shape[0]/2)), interpolation = cv.INTER_CUBIC) 
cv.imshow('Resize2', resize)

cv.waitKey(0)