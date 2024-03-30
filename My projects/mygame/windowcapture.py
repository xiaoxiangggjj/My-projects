import numpy as np
from PIL import ImageGrab
import cv2
import pyautogui


def press_up():
    pyautogui.press('up')
def press_down():
    pyautogui.press('down')
def press_left():
    pyautogui.press('left')
def press_right():
    pyautogui.press('right')

while True:
    # 截取屏幕图片
    screen = np.array(ImageGrab.grab(bbox=(100, 100, 50, 50)))

    # 将图片转换为灰度图像
    #gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    

    # 显示图片
    cv2.imshow('window', screen)

    # 如果按下 q 键，退出循环
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
