import cv2 as cv
import numpy as np

img = cv.imread('pic3.jpg') 

cv.imshow('pic3', img)

def translate(img, x, y): #image, # of pixels you want to shift in x and y axes
    
    transMat = np.float32([[1, 0, x], [0, 1, y]]) #translation matrix
    dimentions = (img.shape[1], img.shape[0]) #(width, height)
    
    return cv.warpAffine(img, transMat, dimentions)

translated = translate(img, 50, 200) 
    
cv.imshow('Translated', translated)

def rotate(img, angle, rotPoint = None):
    (height, width) = (img.shape[0], img.shape[1])
    
    if rotPoint == None:
        rotPoint = (width//2, height//2)
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0) 
    dimentions = (width, height)
    
    return cv.warpAffine(img, rotMat, dimentions)

rotated = rotate(translated, 50) 
    
cv.imshow('Roteted', rotated)

flip = cv.flip(rotated, -1) 

cv.imshow('flipped', flip)


cv.waitKey(0)
