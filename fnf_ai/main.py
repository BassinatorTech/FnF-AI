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
    vertices = numpy.array([[960, 900], [960, 110], [1920, 110], [1920, 900]])
    processed = roi(processed, [vertices])
    cv2.rectangle(processed, (960, 150), (1500, 350), (255, 255, 255), 5)
    return processed


while True:
    screen = numpy.array(ImageGrab.grab(bbox=(0, 0, 1920, 1080)))
    # new_screen = process_img(screen)
    file = cv2.imread("starter_img/up_arrow.png")
    query = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    train = cv2.cvtColor(file, cv2.COLOR_BGR2GRAY)

    orb = cv2.ORB_create()

    query_kp, query_desc = orb.detectAndCompute(query, None)
    train_kp, train_desc = orb.detectAndCompute(train, None)

    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(query_desc, train_desc)
    matches = sorted(matches, key=lambda x: x.distance)

    final = cv2.drawMatches(screen, query_kp, file,
                            train_kp, matches[:10], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

    cv2.imshow("window", cv2.cvtColor(final, cv2.COLOR_BGR2GRAY))
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
