import os
import time
import pyautogui
import keyboard
from PIL import ImageGrab, Image, ImageDraw
from ctypes import *


DIR = os.path.abspath(os.path.dirname(__file__))

# Box Regions
HOLD_TEXT_REGION = [0, 0, 0, 0]
BOBBER_ICON_REGION = [0, 0, 0, 0]
FAILED_FISHING_MESSAGE_REGION = [0, 0, 0, 0]

CONFIDENCE = 0.7


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

    HOLD_TEXT_REGION = [
        int(column_width * 6),#X1
        int(column_height * 6),#Y1
        int(column_width * 8),#X2
        int(column_height * 10),#Y2
    ]
    BOBBER_ICON_REGION = [
        int(column_width * 4),
        int(column_height * 1),
        int(column_width * 8),
        int(column_height * 12),
    ]
    FAILED_FISHING_MESSAGE_REGION = [
        int(column_width * 2),
        int(column_height * 8),
        int(column_width * 8),
        int(column_height * 12),
    ]


def check_ready_to_fish():
    f3_file_path = os.path.join(
        DIR, "external_resources", "image_references", "f3.PNG"
    )
    found = pyautogui.locateCenterOnScreen(f3_file_path, region=tuple(HOLD_TEXT_REGION), grayscale=True, confidence = CONFIDENCE)
    if found:
        return True
    else:
        return False

def check_for_pole():
    # Check screen for fishing pole help text.
    if check_ready_to_fish():
        print("Fishing pole is equiped!")
    else:
        print("Equipping fishing pole...")
        pyautogui.press('f3')
        time.sleep(1.5)


def cast():
    print("Casting...")
    pyautogui.keyUp("b")
    time.sleep(.5)
    pyautogui.keyDown("b")
    pyautogui.mouseDown()
    # Wait for max
    time.sleep(1.89)
    pyautogui.mouseUp()
    # Wait for cast animation
    time.sleep(3)


def wait_for_bite():
    bobber_file_path = os.path.join(
        DIR, "external_resources", "image_references", "bobber.PNG"
    )

    while pyautogui.locateCenterOnScreen(bobber_file_path, region=tuple(BOBBER_ICON_REGION), grayscale=True, confidence = CONFIDENCE) is not None:
        print('Waiting on fish...')
        time.sleep(0.15)

    print("Fish ON!")


def hook_fish():
    time.sleep(0.15)
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


def reel_fish():
    time.sleep(1)
    reeling = True
    green_tension_img = os.path.join(DIR, "external_resources", "image_references", "green_tension.PNG")
    slacked_tension_img = os.path.join(DIR, "external_resources", "image_references", "slacked_tension.PNG")
    while reeling == True:
        while (pyautogui.locateCenterOnScreen(green_tension_img, region=tuple(BOBBER_ICON_REGION), grayscale=True, confidence = 0.8)) or (pyautogui.locateCenterOnScreen(slacked_tension_img, region=tuple(BOBBER_ICON_REGION), grayscale=True, confidence = 0.8)):
            pyautogui.mouseDown()
            if check_ready_to_fish():
                reeling = False
                print("Caught!!!")
                break
        pyautogui.mouseUp()


        # Check Caught
        #FIXME: Relative pixel
        if check_ready_to_fish():
            reeling = False
            print("Caught!!!")
            time.sleep(3)


def main():
    set_regions()

    botting = False

    while True:
        if keyboard.is_pressed("s"):
            botting = True

        while botting == True:
            check_for_pole()
            fishing = True
            while fishing:
                cast()
                wait_for_bite()
                hook_fish()
                reel_fish()

                print("GRATS ON THE BIG FISH!")


if __name__ == "__main__":
    main()
