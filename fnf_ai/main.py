# Started: 3/8/23
# Massive Help: sentdex
# Videos complete: 4
# URL: https://www.newgrounds.com/portal/view/770371

import numpy
import re
from PIL import ImageGrab
import cv2
# import time
from directKeys import *
import pyautogui


def roi(img, vertices):
    mask = numpy.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked


def process_img(img):
    processed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    processed = cv2.Canny(processed, threshold1=200, threshold2=300)
    vertices = numpy.array([[960, 500], [960, 0], [1920, 0], [1920, 500]])
    processed = roi(processed, [vertices])
    return processed


question = input("Are you ready to awake the AI? ")

if re.match("yes", question):
    print("AI is now on")

    while True:
        screen = numpy.array(ImageGrab.grab(bbox=(0, 0, 1920, 1080)))
        new_screen = process_img(screen)
        cv2.imshow("window", new_screen)
        # print("up")
        # PressKey(w)
        # print("release")
        # ReleaseKey(w)
        # cv2.imshow("window", cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
else:
    print("Come back when you're ready")
