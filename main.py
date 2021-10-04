import os
import time
import pyautogui
import keyboard
from PIL import ImageGrab, Image, ImageDraw
from ctypes import *

REEL_COLOR = (26, 161, 127)
WAIT_COLOR_BROWN = (173, 92, 32)
WAIT_COLOR_RED = (62, 16, 18)
HOLD_COLOR_TEXT_WHITE = (252, 252, 252)
COLOR_TOLERANCE = 7

#BOX VARS
HOLD_TEXT_AREA = [0,0,0,0]
BOBBER_ICON_REGION = [0,0,0,0]
FAILED_FISHING_MESSAGE_AREA = [0,0,0,0]

COLUMN_WIDTH = 0
COLUMN_HEIGHT = 0

# Hardware specific functions
def _get_screen_size() -> tuple:
    user32 = windll.user32
    screen_size = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    return screen_size

def _get_center_of_screen() -> tuple:
    screen_size = _get_screen_size()
    center_screen = (int(screen_size[0] / 2), int(screen_size[1] / 2))
    return center_screen

def setup():
    screen_resolution = _get_screen_size()
    number_of_columns = 12
    number_of_rows = 12

    global COLUMN_WIDTH
    COLUMN_WIDTH = screen_resolution[0] / number_of_columns
    global COLUMN_HEIGHT
    COLUMN_HEIGHT = screen_resolution[1] / number_of_rows
    
    global HOLD_TEXT_AREA
    HOLD_TEXT_AREA = [int(COLUMN_WIDTH*6), int(COLUMN_HEIGHT*7), int(COLUMN_WIDTH*8), int(COLUMN_HEIGHT*9)]
    global BOBBER_ICON_REGION
    BOBBER_ICON_REGION = [int(COLUMN_WIDTH*4), int(COLUMN_HEIGHT*1), int(COLUMN_WIDTH*8), int(COLUMN_HEIGHT*12)]
    global FAILED_FISHING_MESSAGE_AREA
    FAILED_FISHING_MESSAGE_AREA = [int(COLUMN_WIDTH*2), int(COLUMN_HEIGHT*8), int(COLUMN_WIDTH*8), int(COLUMN_HEIGHT*12)]
    pass

def test_regions():
    center_screen = _get_center_of_screen()
    top_x = (COLUMN_WIDTH*4)
    top_y = (COLUMN_HEIGHT*1)
    bottom_x = (COLUMN_WIDTH*8)
    bottom_y = (COLUMN_HEIGHT*12)
    screen_cap = ImageGrab.grab(bbox=(top_x, top_y, bottom_x, bottom_y))
    screen_cap.show()

def main():
    center_screen = _get_center_of_screen()

    botting = False
    while True:
        if keyboard.is_pressed('s'):
            botting = True
        while botting == True:
            #Determine if fishing pole is equiped
                #Capture screen
            screen_cap = ImageGrab.grab(bbox=tuple(HOLD_TEXT_AREA))
            hold_text = screen_cap.getpixel((88,30))
                #Check screen for fishing pole help text.
            if hold_text == HOLD_COLOR_TEXT_WHITE:
                print("Fishing pole is equiped!")
            else:
                print("Fishing pole isn't equiped!")
            #TODO: Remove screen capture save debug code.
            #screen_cap.save('C:/Users/Gluttony/Pictures/thefile.jpg')
            #TODO: Remove screen capture display debug code.
            #screen_cap.show()
            #Cast after pole check
                #Right click on screen
                #TODO: Add click variation to disguise botting. (introduce RNG)
            fishing = True
            while fishing:
                pyautogui.mouseDown() #NOTE: Cast
                time.sleep(1.93) #NOTE: Has variance in new world. This will sometimes hit a perfect cast.
                pyautogui.mouseUp() #NOTE: Stop casting

                #TODO: account for animation cast time
                time.sleep(3)
                
                #Determine when to hook fish
                #BBOX(top x, top y, bottom x, bottom y)
                #fishing_bobber_screen_capture = ImageGrab.grab(bbox = (center_screen[0] - 200, center_screen[1] - 400, center_screen[0] + 200, center_screen[1] + 500))

                bobber_icon_position = pyautogui.locateCenterOnScreen('F:/Projects/New World/Autofishing/external_resources/image_references/bobber.PNG',region=tuple(BOBBER_ICON_REGION), grayscale=True)
                print(bobber_icon_position)

                bobber_icon_area = (bobber_icon_position[0] - 50, bobber_icon_position[1] -50, bobber_icon_position[0] + 50, bobber_icon_position[1] + 50)

                #TODO: check if image bounces position
                #Get surrounding pixels around bobber center coords.
                #Use the pixels captured from bobber to determine a change.
                while pyautogui.locateCenterOnScreen('F:/Projects/New World/Autofishing/external_resources/image_references/bobber.PNG', region=bobber_icon_area) is not None:
                    print('waiting on fish')
                    time.sleep(0.15)

                print('Fish ON!')
                #TODO: Fish OFF function
                #NOTE: Hooking the fish section
                time.sleep(0.15)
                pyautogui.mouseDown()
                time.sleep(0.1)
                pyautogui.mouseUp()

                time.sleep(1)
                reeling = True
                while reeling == True:
                    # Check green bobber
                    
                    #Reel Fish In. Great place to introduce a point of failure later.
                    # while green_bobber == true:
                    #     line_tension = True
                    pyautogui.mouseDown()
                    time.sleep(1)
                    pyautogui.mouseUp()
                    time.sleep(0.35)

                    # Check to see if the hold/release icon isn't present.

                # Determine if ready to restart fishing.
                screen_cap = ImageGrab.grab(bbox = (center_screen[0] + 50, center_screen[1] + 150, center_screen[0] + 300, center_screen[1] + 300))
                hold_text = screen_cap.getpixel((88,30))
                if hold_text == HOLD_TEXT_AREA:
                    reeling = False

                print('GRATS ON THE BIG FISH!')
                #Loop while reeling fish in
                # check line for stress
                # delay if stressed
                # reel if not. 
                #while pyautogui.locateCenterOnScreen('F:/Projects/New World/Autofishing/external_resources/image_references/bobber.PNG', region=(bobber_icon_position[0] - 50, bobber_icon_position[1] -50, bobber_icon_position[0] + 50, bobber_icon_position[1] + 500)) is not None:
                
                #fishing = False

                #fishing_bobber_screen_capture.show()

                if keyboard.is_pressed('e'):
                    fishing = False
                    botting = False        
                
            #Reel fish in
                #maintain line strength

if __name__ == "__main__":
    setup()
    main()