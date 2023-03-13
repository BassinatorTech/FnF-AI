# Started: 3/8/23
# Massive Help: sentdex & ClarityCoders
# URL: https://www.newgrounds.com/portal/view/770371

import numpy
import cv2
import keyboard
import pyautogui

# ARROW BAR RGB: (135 163 173) = 471
# LEFT RGB: (194,75,153) = 422
# DOWN RGB: (0,255,255) = 510
# UP RGB: (18,250,5) = 273
# RIGHT RGB: (249,57,63) = 369

while True:
    screen = numpy.array(pyautogui.screenshot(region=(0, 0, 1920, 1500)))

    left = screen[265, 1050]
    if left[0] == 194 and left[1] == 75 and left[2] == 153:
        keyboard.press("left")
    else:
        keyboard.release("left")

    down = screen[265, 1165]
    if down[0] == 0 and down[1] == 255 and down[2] == 255:
        keyboard.press("down")
    else:
        keyboard.release("down")

    up = screen[265, 1280]
    if up[0] == 18 and up[1] == 250 and up[2] == 5:
        keyboard.press("up")
    else:
        keyboard.release("up")

    right = screen[265, 1400]
    if right[0] == 249 and right[1] == 57 and right[2] == 63:
        keyboard.press("right")
    else:
        keyboard.release("right")

    # cv2.imshow("img", cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))

    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
