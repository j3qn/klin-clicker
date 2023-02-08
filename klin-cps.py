import win32api
import win32con
import time
import os
import keyboard
from colorama import init
init()
os.system('cls')
os.system('title ')
logo = """

     /$$   /$$ /$$ /$$          
    | $$  /$$/| $$|__/          
    | $$ /$$/ | $$ /$$ /$$$$$$$ 
    | $$$$$/  | $$| $$| $$__  $$
    | $$  $$  | $$| $$| $$  \ $$
    | $$\  $$ | $$| $$| $$  | $$
    | $$ \  $$| $$| $$| $$  | $$
    |__/  \__/|__/|__/|__/  |__/
            cps multiplier \033[90m


    if you have any issue my discord : jean.#7452

________________________________________________________________________________________________________________________


    \033[0m Cps to multiply? for example (1, 2, 3)
                            
"""
print(logo)
num_clicks = int(input("    > \033[90m"))
print('''
    \033[0m Enter bind to destruct

''')
break_bind = input('    > \033[90m')

os.system('cls')

logo2 = f"""
\033[0m
     /$$   /$$ /$$ /$$          
    | $$  /$$/| $$|__/          
    | $$ /$$/ | $$ /$$ /$$$$$$$ 
    | $$$$$/  | $$| $$| $$__  $$
    | $$  $$  | $$| $$| $$  \ $$
    | $$\  $$ | $$| $$| $$  | $$
    | $$ \  $$| $$| $$| $$  | $$
    |__/  \__/|__/|__/|__/  |__/
            cps multiplier \033[90m


    Multiply Number : \033[91m{num_clicks}\033[90m
    Bind to destruct : \033[91m{break_bind}\033[90m

________________________________________________________________________________________________________________________
                            
"""

print(logo2)


def click():
    x, y = win32api.GetCursorPos()
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

click_delay = 0.001

while True:
    if keyboard.is_pressed(break_bind):
        exit()
    if win32api.GetKeyState(0x01) & 0x8000:
        while win32api.GetKeyState(0x01) & 0x8000:
            for i in range(num_clicks):
                click()
                time.sleep(click_delay)
    time.sleep(0.1)