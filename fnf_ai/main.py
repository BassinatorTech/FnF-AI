# Started: 3/8/23
# Massive Help: sentdex
# Videos completed: 6
# URL: https://www.newgrounds.com/portal/view/770371
# Direct Keys: https://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game

import numpy
import re
from PIL import ImageGrab
import cv2
# import time
import keyboard
import pyautogui


# REGION-OF-INTEREST
def roi(img, vertices):
    mask = numpy.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked


def process_img(img):
    processed = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    processed = cv2.Canny(processed, threshold1=200, threshold2=300)
    processed = cv2.GaussianBlur(processed, (5, 5), 0)
    vertices = numpy.array([[960, 900], [960, 0], [1920, 0], [1920, 900]])
    processed = roi(processed, [vertices])
    return processed


# COMPUTER VISION
while True:
    screen = numpy.array(ImageGrab.grab(bbox=(0, 0, 1920, 1080)))
    new_screen = process_img(screen)
    cv2.imshow("window", new_screen)
    # cv2.imshow("window", cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
