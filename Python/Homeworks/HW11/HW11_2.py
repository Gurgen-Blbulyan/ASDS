import cv2 as cv
import numpy as np

img = cv.imread('pic1.jpg') 

cv.imshow('pic1', img) 

b, g, r = cv.split(img)



blank = np.zeros(img.shape[:2], dtype = 'uint8')
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

bg=cv.cvtColor(blue, cv.COLOR_BGR2GRAY)
gg=cv.cvtColor(green, cv.COLOR_BGR2GRAY)
rg=cv.cvtColor(red, cv.COLOR_BGR2GRAY)

cv.imshow('blueg', bg)
cv.imshow('greeng', gg)
cv.imshow('redg', rg)

cv.waitKey(0)