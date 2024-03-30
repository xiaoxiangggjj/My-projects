
import cv2 as cv
import numpy as np
import os
import time
from windowcapture import WindowCapture
import pyautogui

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def pressSpaceButton():
    time.sleep(0.15)
    pyautogui.keyDown('space')
    pyautogui.keyUp('space')
def match(haystack_img,needle_img):

# There are 6 comparison methods to choose from:
# TM_CCOEFF, TM_CCOEFF_NORMED, TM_CCORR, TM_CCORR_NORMED, TM_SQDIFF, TM_SQDIFF_NORMED
# You can see the differences at a glance here:
# https://docs.opencv.org/master/d4/dc6/tutorial_py_template_matching.html
# Note that the values are inverted for TM_SQDIFF and TM_SQDIFF_NORMED
    result = cv.matchTemplate(haystack_img, needle_img, cv.TM_SQDIFF_NORMED)

# I've inverted the threshold and where comparison to work with TM_SQDIFF_NORMED
    threshold = 0.28
# The np.where() return value will look like this:
# (array([482, 483, 483, 483, 484], dtype=int32), array([514, 513, 514, 515, 514], dtype=int32))
    locations = np.where(result <= threshold)
# We can zip those up into a list of (x, y) position tuples
    locations = list(zip(*locations[::-1]))
    #print(locations)

    if locations:
        print('Found needle.')

        needle_w = needle_img.shape[1]
        needle_h = needle_img.shape[0]
        line_color = (0, 255, 0)
        line_type = cv.LINE_4

    # Loop over all the locations and draw their rectangle
        for loc in locations:
        # Determine the box positions
            top_left = loc
            bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
        # Draw the box
            cv.rectangle(haystack_img, top_left, bottom_right, line_color, line_type)

        #cv.imshow('Matches', haystack_img)
        return haystack_img
    #cv.imwrite('result.jpg', haystack_img)

    else:
        return haystack_img
def get_feature(img):
    fearture_img = img[430:550,120:260]
    return fearture_img
def press_up():
    pyautogui.press('up')
def press_down():
    pyautogui.press('down')
def press_left():
    pyautogui.press('left')
def press_right():
    pyautogui.press('right')                                
# initialize the WindowCapture class
wincap = WindowCapture('my first game')
#needle_img = cv.imread('32.png', cv.IMREAD_COLOR)
loop_time = time.time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    #get_screenshot = wincap.get_screen_position((100,400))
    #img = match(screenshot, needle_img)
    my_img = get_feature(screenshot)
    gay_img = cv.cvtColor(my_img, cv.COLOR_BGR2GRAY)
    print(gay_img[0][10])
    cv.imshow('Computer Vision', my_img)
    if gay_img[0][10] == 35:
        press_up()
    if gay_img[0][10] == 94:
        press_down()
    if gay_img[0][10] == 76:
        press_right()
    if gay_img[0][10] == 226:
        press_left()
    #cv.imshow('goal_screenshot',get_screenshot)
    #pressSpaceButton()
    # debug the loop rate


    print('FPS {}'.format(1 / (time.time() - loop_time)))
    loop_time = time.time()
    #pyautogui.press('space')
    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    #time.sleep(0.05)
    
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')
