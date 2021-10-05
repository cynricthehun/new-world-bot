import os
import time
import pyautogui
import keyboard
from PIL import ImageGrab, Image, ImageDraw
from ctypes import *


DIR = os.path.abspath(os.path.dirname(__file__))

# Colors
HOLD_COLOR_TEXT_WHITE = (252, 252, 252)

# Box Regions
HOLD_TEXT_REGION = [0,0,0,0]
BOBBER_ICON_REGION = [0,0,0,0]
FAILED_FISHING_MESSAGE_REGION = [0,0,0,0]


# Hardware specific functions
def get_screen_size() -> tuple:
    user32 = windll.user32
    screen_size = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    return screen_size


def get_center_of_screen() -> tuple:
    screen_size = get_screen_size()
    center_screen = (int(screen_size[0] / 2), int(screen_size[1] / 2))
    return center_screen


def set_regions():
    global HOLD_TEXT_REGION
    global BOBBER_ICON_REGION
    global FAILED_FISHING_MESSAGE_REGION

    screen_resolution = get_screen_size()
    number_of_columns = 12
    number_of_rows = 12

    column_width = screen_resolution[0] / number_of_columns
    column_height = screen_resolution[1] / number_of_rows
    
    HOLD_TEXT_REGION = [int(column_width*6), int(column_height*7), int(column_width*8), int(column_height*9)]
    BOBBER_ICON_REGION = [int(column_width*4), int(column_height*1), int(column_width*8), int(column_height*12)]
    FAILED_FISHING_MESSAGE_REGION = [int(column_width*2), int(column_height*8), int(column_width*8), int(column_height*12)]


def check_for_pole():
    screen_cap = ImageGrab.grab(bbox=tuple(HOLD_TEXT_REGION))
    screen_cap.show()
    hold_text = screen_cap.getpixel((88,30))
        #Check screen for fishing pole help text.
    if hold_text == HOLD_COLOR_TEXT_WHITE:
        print("Fishing pole is equiped!")
    else:
        print("Fishing pole isn't equiped!")


def cast():
    pyautogui.mouseDown()
    # Wait for max
    time.sleep(1.91)
    pyautogui.mouseUp()
    # Wait for cast animation
    time.sleep(3)


def wait_for_bite():
    bobber_file_path = os.path.join(DIR, "external_resources", "image_references", "bobber.PNG")

    while pyautogui.locateCenterOnScreen(bobber_file_path, region=tuple(BOBBER_ICON_REGION), grayscale=True, confidence = 0.7) is not None:
        print('Waiting on fish...')
        time.sleep(0.15)

    print('Fish ON!')


def hook_fish():
    time.sleep(0.15)
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


def reel_fish():
    time.sleep(1)
    reeling = True
    while reeling == True:
        pyautogui.mouseDown()
        time.sleep(1)
        pyautogui.mouseUp()
        time.sleep(0.35)
        screen_cap = ImageGrab.grab(bbox = (center_screen[0] + 50, center_screen[1] + 150, center_screen[0] + 300, center_screen[1] + 300))
        hold_text = screen_cap.getpixel((88,30))
        if hold_text == HOLD_TEXT_AREA:
            reeling = False


def main():
    center_screen = get_center_of_screen()
    set_regions()

    botting = False

    while True:
        if keyboard.is_pressed('s'):
            botting = True
        while botting == True:
            check_for_pole()
            #Determine if fishing pole is equiped
                #Capture screen
            
            #TODO: Remove screen capture save debug code.
            #screen_cap.save('C:/Users/Gluttony/Pictures/thefile.jpg')
            #TODO: Remove screen capture display debug code.
            #screen_cap.show()
            #Cast after pole check
                #Right click on screen
                #TODO: Add click variation to disguise botting. (introduce RNG)
            fishing = True
            while fishing:
                cast()
                wait_for_bite()
                hook_fish()
                reel_fish()
                

                    # Check to see if the hold/release icon isn't present.

                # Determine if ready to restart fishing.
                

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
    main()
    #test_regions()