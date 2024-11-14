import cv2 as cv2
import numpy as np

input_path = "/home/malte/Documents/Programming Projects/Baumy/Baumy/InputPictures/Input.jpeg"


## img laden
img = cv2.imread(input_path)
img = cv2.resize(img, (500 , 500))

if img is None:
    print("Image not found or path is incorrect")
else:
    print("Image loaded successfully")

def get_brightest_pixels(img):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('GrayImage', gray_image)
    cv2.waitKey(0)

    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray_image)

    cv2.circle(img, maxLoc, radius=5, color=(0, 0, 255), thickness=-1)

    return maxLoc

maxLoc = get_brightest_pixels(img)
print(maxLoc)
cv2.imshow('Brightest Pixel', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
