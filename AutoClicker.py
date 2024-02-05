import pyautogui
import keyboard
import time

def auto_click(num_clicks, interval):
    print("Start AutoClicker (F6 "
          "End AutoClicker HOLD F7)")
    while True:
        keyboard.wait("F6")
        for _ in range(num_clicks):
            if keyboard.is_pressed("F7"):
                return
            print("AutoClicer: Clicked Succesfully!")
            pyautogui.click()
            time.sleep(interval)


    print("AutoClicker: Ended Clicking Succesfully!")

num_clicks = 50
interval = 0.1
auto_click(num_clicks, interval)