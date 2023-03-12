# Started: 3/8/23
# Massive Help: sentdex & ClarityCoders
# URL: https://www.newgrounds.com/portal/view/770371

import numpy
from PIL import ImageGrab
import cv2
import keyboard
import time

left = {
    "press": False,
    "loc": (1050, 265),
    "key": "left"
}
down = {
    "press": False,
    "loc": (1165, 265),
    "key": "down"
}
up = {
    "press": False,
    "loc": (1280, 265),
    "key": "up"
}
right = {
    "press": False,
    "loc": (1400, 265),
    "key": "right"
}

# LEFT RGB: (194,75,153) = 422
# DOWN RGB: (0,255,255) = 510
# UP RGB: (18,250,5) = 273
# RIGHT RGB: (249,57,63) = 369

while True:
    screen = numpy.array(ImageGrab.grab(bbox=(0, 0, 1920, 1500)))

    dot_coords = [(1050, 265), (1165, 265), (1280, 265), (1400, 265)]
    for coords in dot_coords:
        cv2.circle(screen, coords, 10, (255, 255, 255), -1)
        cv2.imshow("img", cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))

    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
