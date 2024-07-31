import pyautogui as pag
import time
import random
import keyboard  # Step 1: Import the keyboard library

def jiggle_mouse():
    running = True  # Step 2: Initialize a flag to control the loop
    while running:
        if keyboard.is_pressed('esc'):  # Step 3: Check if the escape key is pressed
            running = False  # Change the flag to stop the loop
            break  # Immediately exit the loop
        x = random.randint(600, 700)
        y = random.randint(200, 600)
        pag.moveTo(x, y, 0.5)
        time.sleep(1)

if __name__ == "__main__":
    jiggle_mouse()