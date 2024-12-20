import cv2 as cv2
import numpy as np
from cv2 import VideoCapture, waitKey, destroyWindow


class Picture:

    def __init__(self):
        self.img = None
        self.img_brightestpixel = None
        self.brightestpixel = None

    def load_picture(self, input_path):
        self.img = cv2.imread(input_path)
        print("Picture Loaded")

    def display_picture(self):
        if self.img is None: print("no Image loaded")
        else:
            cv2.imshow("Image", self.img)
            cv2.waitKey(0)

    def resize_picture(self, width, height):
            self.img = cv2.resize(self.img, (width , height))

    def calculate_brightest_pixel(self):
        if self.img is None: print("Image not found or path is incorrect")
        gray_image = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        gray_gaussian = cv2.GaussianBlur(gray_image,(5,5),0)
        cv2.imshow("Image", gray_gaussian)

        (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray_gaussian)

        self.brightestpixel = (maxLoc, maxVal)

        self.img_brightestpixel = self.img.copy()
        cv2.circle(self.img_brightestpixel, maxLoc, radius=5, color=(0, 0, 255), thickness=-1)
        cv2.waitKey(0)

        return self.brightestpixel

    def show_brightest_pixel(self):
        if self.img is None: print("Brightes Pixel Image not found")
        cv2.imshow('Brightest Pixel', self.img_brightestpixel)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def get_brightest_pixel(self):
        return self.brightestpixel

    def takePicture(self, cam_source):
        cam = VideoCapture(cam_source)
        #cam = cv2.VideoCapture("/dev/video2")  # check this
        # Get the default frame width and height
        frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

        result, image = cam.read()

        if result:
            self.img = image
            #cv2.imshow("Test", self.img)
        else:
            print("No image detected. Please! try again")

input_path = "/home/malte/Documents/Programming Projects/Baumy/Baumy/InputPictures/Input.jpg"

debug = False
if (debug == True):
    pic = Picture()
    #pic.load_picture("/home/malte/Documents/Programming Projects/Baumy/Baumy/InputPictures/Input.jpg")
    #pic.display_picture()
    #pic.calculate_brightest_pixel()
    #pic.show_brightest_pixel()
    pic.takePicture("/dev/video0")
    pic.calculate_brightest_pixel()
    pic.show_brightest_pixel()
    #pic.display_picture()
