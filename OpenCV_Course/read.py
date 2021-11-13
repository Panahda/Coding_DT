import cv2 as cv

# Reading images
img = cv.imread('Images/cat_3_L.jpg')
cv.imshow('cat_3_L', img)

cv.waitKey(0)

# Reading Videos
capture = cv.VideoCapture('Vids/dog_v_1.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
