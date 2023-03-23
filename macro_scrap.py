import re 
import keyboard
import pyautogui
import time


def click_and_process():
    time.sleep(1)
    pyautogui.click(pyautogui.position())
    time.sleep(3)
    pyautogui.moveTo(1400,480, duration = 1)
    pyautogui.click(pyautogui.position())
    keyboard.press_and_release('ctrl+f')
    time.sleep(1)
    time.sleep(2)
    keyboard.write('m3u8')
    time.sleep(0.5)
    keyboard.press_and_release('enter')
    time.sleep(0.5)
    pyautogui.click(pyautogui.position())
    time.sleep(0.5)
    keyboard.press_and_release('ctrl+c')
    time.sleep(0.5)
    keyboard.press_and_release('windows+1')
    time.sleep(0.5)
    keyboard.press_and_release('ctrl + end')
    time.sleep(0.5)
    
    keyboard.press_and_release('enter')
    time.sleep(0.5)
    keyboard.press_and_release('ctrl+v')
    time.sleep(0.5)
    keyboard.press_and_release('ctrl+s')
    time.sleep(1)
    keyboard.press_and_release('windows+2')
    time.sleep(2)
    pyautogui.moveTo(600,410, duration = 2)
    time.sleep(0.5)
    pyautogui.click(pyautogui.position())
    time.sleep(2)
    keyboard.press_and_release('alt+ Left arrow')
    time.sleep(2)
def to_right():
    pyautogui.moveTo(650,890, duration = 1)
    
def to_left():
    pyautogui.moveTo(400,890, duration = 1)

def jump():
    pyautogui.scroll(-470)
def multiple_jump():
    pyautogui.scroll(-770)
def cycle_1():
    to_right()
    click_and_process()
    to_right()
    jump()
    to_right()
    click_and_process()
    to_left()
    click_and_process()
    to_left()
    jump()
    to_left()
    click_and_process()
    to_right()
    click_and_process()
    to_right()
    multiple_jump()
    to_right()
    click_and_process()
def cycle_2():
    to_left()
    click_and_process()
    to_left()
    jump()
    click_and_process()
    to_right()
    click_and_process()
    to_right()
    jump()
    click_and_process()
    to_left()
    click_and_process()
    to_left()
    multiple_jump()
    click_and_process()
def lastcycle():
    multiple_jump()
    pyautogui.moveTo(650,850, duration = 1)
    click_and_process()
    pyautogui.moveTo(400,850, duration = 1)
    pyautogui.moveTo(400,290, duration = 1)
    pyautogui.moveTo(650,950, duration = 1)
    click_and_process()
    pyautogui.moveTo(400,950, duration = 1)
    click_and_process()
to_left()
click_and_process()
for i in range(1,9):
    cycle_1()
    cycle_2()
    print(f'cycle -{i}')

# https://5a2f.tianliplanner.com/
def filter_link_m3u8():
    time.sleep(3)
    f = open("html.txt", "r")
    data = f.readlines()
    for x in data :
        result = re.search(r'((http|https):)[A-Z0-9a-z\.\/_]*(\.m3u8)', x)
        if result:
            url = result.group(0)
            with open('tianliplanner_list_link_video.txt', 'a', encoding='utf-8') as f:
                f.write(f'{url}\n\n')
