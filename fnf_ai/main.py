# Started: 3/8/23
# Massive Help: sentdex
# Videos completed: 6
# URL: https://www.newgrounds.com/portal/view/770371
# Direct Keys: https://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game

import numpy
import re
import time
from PIL import ImageGrab
import cv2
import keyboard
import pyautogui


def key(key):
    keyboard.press(key)
    keyboard.release(key)


# REGION-OF-INTEREST
def roi(img, vertices):
    mask = numpy.zeros_like(img)
    cv2.fillPoly(mask, vertices, 255)
    masked = cv2.bitwise_and(img, mask)
    return masked


def process_img(img):
    processed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    processed = cv2.Canny(processed, threshold1=200, threshold2=300)
    processed = cv2.GaussianBlur(processed, (5, 5), 0)
    vertices = numpy.array([[960, 900], [960, 110], [1920, 110], [1920, 900]])
    processed = roi(processed, [vertices])
    cv2.rectangle(processed, (960, 150), (1500, 350), (255, 255, 255), 5)
    return processed


while True:
    screen = numpy.array(ImageGrab.grab(bbox=(900, 0, 1920, 1080)))
    # new_screen = process_img(screen)
    gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    template = cv2.imread("starter_img/arrow_bar_1.png", 0)
    w, h = template.shape[::-1]
    threshold = 0.8
    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    loc = numpy.where(res >= threshold)
    for pt in zip(*loc[:: -1]):
        cv2.rectangle(screen, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)

    cv2.imshow("window", cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY))
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
