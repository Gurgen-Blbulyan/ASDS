import cv2 as cv
import numpy as np

blank = np.zeros((400, 400, 3), dtype='uint8')

rectangle1 = cv.rectangle(blank.copy(), (30, 30), (370, 370), (130, 130, 130), -1)
rectangle2 = cv.rectangle(blank.copy(), (30, 30), (370, 370), (100, 0, 250), -1)

circle1 = cv.circle(blank.copy(), (200, 200), 200, (130, 130, 130), -1)
circle2 = cv.circle(blank.copy(), (200, 200), 200, (100, 0, 250), -1)

bitwise_1 = cv.bitwise_xor(rectangle1, circle1)
bitwise_2 = cv.bitwise_or(rectangle1, circle1)
bitwise_3 = cv.bitwise_xor(rectangle2, circle2)

cv.imshow('bitwise_1', bitwise_1)
cv.imshow('bitwise_2', bitwise_2)
cv.imshow('bitwise_3', bitwise_3)

cv.waitKey(0)