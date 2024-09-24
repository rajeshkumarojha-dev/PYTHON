import pyautogui
import time
time.sleep(2)

count=0
while count<=500:
    pyautogui.typewrite("Good afternoon")
    pyautogui.press("enter")
    count = count+1

    # code for auto generate text in whatsapp