import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
# cv.imshow('Blank', blank) : show the blank image

# 1.  paint the image to a certain colour
blank[200:300, 300:400] = 0, 255, 0
cv.imshow('Green', blank)

# 2. draw a rectangle
cv. rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness=3)
cv.imshow('rectangle', blank)

# 3. draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=-1)
cv.imshow('circle', blank)

# 4. draw a line
cv.line(blank, (0, 0), (300, 400), (255, 255, 255), thickness=3)
cv.imshow('line', blank)

# 5. write text
cv.putText(blank, 'Hello, ni hao,zzz', (100, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (205, 255, 255), thickness=2)
cv.imshow('text', blank)

cv.waitKey(0)
