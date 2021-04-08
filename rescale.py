import cv2 as cv


def Rescale(frame, scale=0.75):
    # FOR PICTURES,VIDEO,LIVE
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


def CHANGE_RES(width, height):
    # FOR LIVE FEED
    cv.capture.set(3, width)
    cv.capture.set(4, height)


def VIDEO():
    video = cv.VideoCapture('Videos/dog.mp4')
    while True:
        istrue, frame = video.read()
        resized = Rescale(frame)
        cv.imshow('dog', resized)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break


def PICTURE():
    image = cv.imread('Photos/cat_large.jpg')
    resized = Rescale(image, scale=.4)
    cv.imshow('CAT', resized)
    cv.waitKey(0)


PICTURE()
