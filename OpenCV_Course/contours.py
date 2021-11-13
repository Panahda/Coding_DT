import cv2 as cv
import numpy as np

img = cv.imread('Images/cat_3_L.jpg')
resized = cv.resize(img, (1000, 700), interpolation=cv.INTER_AREA)

blank = np.zeros(resized.shape, dtype='uint8')
# cv.imshow('Blank', blank)

gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)


ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# RETRE_LIST = ALL CONTOURS
# RETRE_EXTERNAL = EXTERNAL CONTOURS
# RETRE_TREE = HIERARCHICAL CONTOURS
# CHAIN_APPROX_SIMPLE = compress contours in line to endpoints

print(f'{len(contours)} contours found')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)
