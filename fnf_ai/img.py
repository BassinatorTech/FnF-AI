import cv2
import numpy
import pyautogui

img = numpy.array(pyautogui.screenshot(region=(0, 0, 1920, 1500)))

rgb = img[265, 1280]
print(rgb)

dot_coords = [(1050, 265), (1165, 265), (1280, 265), (1400, 265)]
for coords in dot_coords:
    cv2.circle(img, coords, 10, (255, 255, 255), -1)
    cv2.imshow("img", cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
cv2.waitKey(0)
cv2.destroyAllWindows()
