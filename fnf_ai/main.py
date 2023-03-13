import cv2
import numpy
import keyboard
import pyautogui

# LEFT RGB: (194,75,153)
# LEFT LINE RGB: (170 110 161)

# LEFT RGB PIXELATED: (226 118 255)
# LEFT LINE RGB PIXELATED: (201 145 233)

# DOWN RGB: (0,255,255)
# DOWN LINE RGB: (54 218 222)

# DOWN RGB PIXELATED: (61 202 255)
# DOWN LINE RGB PIXELATED: (102 195 233)

# UP RGB: (18,250,5)
# UP LINE RGB: (65 215 72)

# UP RGB PIXELATED: (113 227 0)
# UP LINE RGB PIXELATED: (133 210 80)

# RIGHT RGB: (249,57,63)
# RIGHT LINE RGB: (203  99 107)

# RIGHT RGB PIXELATED: (255 136 78)
# RIGHT LINE RGB PIXELATED: (218 156 127)

while True:
    screen = numpy.array(pyautogui.screenshot(region=(0, 0, 1920, 1500)))

    left = screen[265, 1050]
    if left[0] == 194 and left[1] == 75 and left[2] == 153 or left[0] == 170 and left[1] == 110 and left[2] == 161:
        keyboard.press("left")
    elif left[0] == 226 and left[1] == 118 and left[2] == 255 or left[0] == 201 and left[1] == 145 and left[2] == 233:
        keyboard.press("left")
    else:
        keyboard.release("left")

    down = screen[265, 1165]
    if down[0] == 0 and down[1] == 255 and down[2] == 255 or down[0] == 54 and down[1] == 218 and down[2] == 222:
        keyboard.press("down")
    elif down[0] == 61 and down[1] == 202 and down[2] == 255 or down[0] == 102 and down[1] == 195 and down[2] == 233:
        keyboard.press("down")
    else:
        keyboard.release("down")

    up = screen[265, 1280]
    if up[0] == 18 and up[1] == 250 and up[2] == 5 or up[0] == 65 and up[1] == 215 and up[2] == 72:
        keyboard.press("up")
    elif up[0] == 113 and up[1] == 227 and up[2] == 0 or up[0] == 133 and up[1] == 210 and up[2] == 80:
        keyboard.press("up")
    else:
        keyboard.release("up")

    right = screen[265, 1400]
    if right[0] == 249 and right[1] == 57 and right[2] == 63 or right[0] == 203 and right[1] == 99 and right[2] == 107:
        keyboard.press("right")
    elif right[0] == 255 and right[1] == 136 and right[2] == 78 or right[0] == 218 and right[1] == 156 and right[2] == 127:
        keyboard.press("right")
    else:
        keyboard.release("right")

    # cv2.imshow("img", cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))

    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
