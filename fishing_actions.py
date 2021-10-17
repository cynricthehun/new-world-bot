import os
import pyautogui
import time

CAMERA_LOOK_KEY = "b"

def fishing_loop(configs):
    fishing = True
    while fishing:
        # repair_check()
        cast()
        wait_for_bite(configs.bobber_img, configs.bobber_region)
        hook_fish()
        reel_fish(configs)
        wait_for_ready(configs.f3_img, configs.hold_text_region)


def check_ready_to_fish(f3_img, hold_text_region):
    found = pyautogui.locateCenterOnScreen(
        f3_img, region=tuple(hold_text_region), grayscale=True, confidence=0.7
    )
    if found:
        return True
    else:
        return False


def cast():
    print("Casting...")
    pyautogui.keyUp(CAMERA_LOOK_KEY)
    time.sleep(0.5)
    pyautogui.keyDown(CAMERA_LOOK_KEY)
    pyautogui.mouseDown()
    # Wait for max cast
    time.sleep(1.89)
    pyautogui.mouseUp()
    # Wait for cast animation
    time.sleep(3)


def wait_for_bite(bobber_img, bobber_region):
    while (
        pyautogui.locateCenterOnScreen(
            bobber_img, region=tuple(bobber_region), grayscale=True, confidence=0.7
        )
        is not None
    ):
        print("Waiting on fish...")
        time.sleep(0.15)

    print("Fish ON!")


def hook_fish():
    time.sleep(0.15)
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.mouseUp()


def reel_fish(configs):
    time.sleep(1)
    reeling = True

    while reeling == True:
        while (
            pyautogui.locateCenterOnScreen(
                configs.green_tension_img,
                region=tuple(configs.bobber_region),
                grayscale=True,
                confidence=0.8,
            )
        ) or (
            pyautogui.locateCenterOnScreen(
                configs.slacked_tension_img,
                region=tuple(configs.bobber_region),
                grayscale=True,
                confidence=0.75,
            )
        ):
            pyautogui.mouseDown()
            if check_ready_to_fish(configs.f3_img, configs.hold_text_region):
                reeling = False
                print("Caught!!!")
                break
        pyautogui.mouseUp()
        if check_ready_to_fish(configs.f3_img, configs.hold_text_region):
            reeling = False
            print("Caught!!!")
            time.sleep(1)


def repair_check(repair_img, repair_region):
    # TODO:check dura

    if pyautogui.locateOnScreen(
        repair_img, region=tuple(repair_pole_region), grayscale=True, confidence=0.7
    ):
        print("Need to Repair")
        # TODO:repair
        # open inventory
        keyboard.press("tab")
        time.sleep(0.1)
        keyboard.release("tab")
        time.sleep(0.1)
        # r+click pole (1160,890) column_width*5.44 column_height*7.42
        pyautogui.moveTo(1160, 890, 0.5)
        keyboard.press("r")
        time.sleep(0.1)
        pyautogui.mouseDown()
        time.sleep(0.1)
        pyautogui.mouseUp()
        time.sleep(0.1)
        keyboard.release("r")
        time.sleep(0.1)
        # e (confirm repair)
        keyboard.press("e")
        time.sleep(0.1)
        keyboard.release("e")
        # close inventory
        keyboard.press("tab")
        time.sleep(0.1)
        keyboard.release("tab")
        time.sleep(2)
        pyautogui.press("f3")
        time.sleep(0.5)


def wait_for_ready(f3_img, hold_text_region):
    while (
        pyautogui.locateCenterOnScreen(
            f3_img, region=tuple(hold_text_region), grayscale=True, confidence=0.7
        )
        is None
    ):
        print("Waiting for ready...")
        time.sleep(0.5)
