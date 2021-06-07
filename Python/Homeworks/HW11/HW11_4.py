import cv2 as cv
import numpy as np


img = cv.imread('pic2.jpg') 
blank = np.zeros(img.shape[:2], dtype = 'uint8')

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 70, 255, -1)

cv.imshow('original', img) 
cv.imshow('mask', mask) 

masked_image = cv.bitwise_and(img, img, mask=mask)

cv.imshow('original image', img) 
cv.imshow('result', masked_image) 

cv.waitKey(0)