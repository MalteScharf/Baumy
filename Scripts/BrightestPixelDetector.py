import cv2 as cv2
import numpy as np
from cv2 import VideoCapture, waitKey, destroyWindow

input_path = "/home/malte/Documents/Programming Projects/Baumy/Baumy/InputPictures/Input.jpeg"
## img laden
img = cv2.imread(input_path)
img = cv2.resize(img, (500 , 500))



def get_brightest_pixels(img):
    if img is None:
        print("Image not found or path is incorrect")
    else:
        print("Image loaded successfully")
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('GrayImage', gray_image)
    cv2.waitKey(0)

    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray_image)

    cv2.circle(img, maxLoc, radius=5, color=(0, 0, 255), thickness=-1)

    return maxLoc, maxVal

def takePicture():
    cam = VideoCapture(0)
    # Get the default frame width and height
    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    result, image = cam.read()

    if result:
        cv2.imshow("Test", image)
        cv2.imwrite("Test", image)
        waitKey(0)
        destroyWindow("Test")
    else:
        print("No image detected. Please! try again")

takePicture()
## maxLoc = get_brightest_pixels(img)
#print(maxLoc)
#cv2.imshow('Brightest Pixel', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
