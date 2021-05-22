import cv2 as cv

img = cv.imread('pic2.jpg') 

cv.imshow('pic2', img)

canny = cv.Canny(img, 125, 175)
cv.imshow('Edges', canny)

blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT) 
canny = cv.Canny(blur, 125, 175)
cv.imshow('Edges_blured', canny)

cv.waitKey(0)
