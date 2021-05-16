import cv2 as cv

img = cv.imread('pic1.jpg')
img1 = cv.imread('pic1.jpg')

cv.line(img, (0,img.shape[0]), (img.shape[1], 0), 
				(255, 255, 0), thickness = 3)

cv.imshow('Original', img1)
cv.imshow('Line', img)


cv.waitKey(0)