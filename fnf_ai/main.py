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


upper_colors = {
    "red": numpy.array([10, 255, 255]),
    "blue": numpy.array([130, 255, 255]),
    "purple": numpy.array([170, 255, 255]),
    "green": numpy.array([80, 255, 255])
}

lower_colors = {
    "red": numpy.array([0, 50, 50]),
    "blue": numpy.array([90, 50, 50]),
    "purple": numpy.array([130, 50, 50]),
    "green": numpy.array([40, 50, 50])
}


while True:
    screen = numpy.array(ImageGrab.grab(bbox=(0, 0, 1920, 1080)))

    hsv = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
    arrows = []
    for color in lower_colors.keys():
        mask = cv2.inRange(hsv, lower_colors[color], upper_colors[color])
        contours, hierarchy = cv2.findContours(
            mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 500:
                x, y, w, h = cv2.boundingRect(contour)
                if w > 20 and h > 20:
                    arrow = {
                        "color": color,
                        "x": x,
                        "y": y,
                        "w": w,
                        "h": h
                    }
                    arrows.append(arrow)
    new_screen = process_img(screen)
    for arrow in arrows:
        x, y, w, h = arrow["x"], arrow["y"], arrow["w"], arrow["h"]
        color = arrow["color"]
        cv2.rectangle(new_screen, (x, y), (x + w, y + h), (255, 0, 0), 3)
        cv2.putText(new_screen, color, (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow("window", new_screen)
    # cv2.imshow("window", cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
