import cv2 as cv


# rescale function (img + vid + live vid)
def rescale_frame(frames, scale=0.75):
    width = int(frames.shape[1] * scale)
    height = int(frames.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frames, dimensions, interpolation=cv.INTER_AREA)


# rescale function (live vid)
def change_res(width, height):
    capture.set(3, width)
    capture.set(4, height)


# Image
img = cv.imread('Images/cat_3_L.jpg')
cv.imshow('cat_3_L', img)

resized_image = rescale_frame(img)
cv.imshow('Cat_3_L_resized', resized_image)

cv.waitKey(0)


# Video
capture = cv.VideoCapture('Vids/dog_v_1.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescale_frame(frame)

    cv.imshow('Video', frame)
    cv.imshow('Video_Resized', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
