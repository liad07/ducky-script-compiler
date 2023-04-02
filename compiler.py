import pyautogui
import time
import sys

# ducky script compiler

y = open("example.ds", 'r')
lines = y.readlines()


def runer(comand, line):
    line2 = " ".join(line)
    commands = ['ENTER', 'TAB', 'SHIFT', 'ALT', 'CONTROL', 'MENU', 'INSERT', 'HOME', 'END', 'PAGEUP', 'PAGEDOWN',
                'DELETE', 'CAPSLOCK', 'NUMLOCK', 'SCROLLLOCK', 'ESCAPE', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8',
                'F9', 'F10', 'F11', 'F12']

    if comand == "DELAY":
        delay_value = line2.replace(comand, "").strip().replace(" ", "")
        time.sleep(float(delay_value) / 1000)

    if comand == "STRING":
        pyautogui.write(line2.replace(comand, "").strip())
    if comand == "GUI":
        if sys.platform == "win32":
            # windows
            pyautogui.hotkey("winleft", line2.replace(comand, "").strip())
        elif sys.platform == "darwin":
            # macOS platform
            pyautogui.hotkey("command", line2.replace(comand, ""))
    if comand in commands:
        pyautogui.press(comand)
    if comand == "REPEAT":
        times = int(line2.replace(comand, "").strip())

        text = "".join(lines).replace(str(times), "")

        start_word = "REPEAT"
        end_word = "ENDREPEAT"
        start_index = text.index(start_word) + len(start_word)
        end_index = text.index(end_word)
        result = text[start_index:end_index].strip()
        print(result)
        for i in range(times-1):
            linesof = result.split("\n")
            print(len(linesof))
            for j in range(len(linesof)):
                runer(linesof[j].split(" ")[0], linesof[j].replace(linesof[j].split(" ")[0].strip(), "").strip().replace(" ",""))

for i in range(len(lines)):
    comand = lines[i].split(" ")[0]
    z = lines[i].split(" ")
    runer(comand, z)
    
# REM: Used for adding comments in the script.
# DELAY: Used for adding delays between keystrokes or commands.
# STRING: Used for typing out a string of characters.
# GUI: Used for pressing the Windows or Command key.
# ENTER: Used for pressing the Enter key.
# TAB: Used for pressing the Tab key.
# SHIFT: Used for pressing the Shift key.
# ALT: Used for pressing the Alt key.
# CONTROL: Used for pressing the Control key.
# REPEAT: Used for repeating a command a specified number of times.
# MENU: Used for pressing the Menu/Apps key.
# INSERT: Used for pressing the Insert key.
# HOME: Used for pressing the Home key.
# END: Used for pressing the End key.
# PAGEUP: Used for pressing the Page Up key.
# PAGEDOWN: Used for pressing the Page Down key.
# DELETE: Used for pressing the Delete key.
# CAPSLOCK: Used for pressing the Caps Lock key.
# NUMLOCK: Used for pressing the Num Lock key.
# SCROLLLOCK: Used for pressing the Scroll Lock key.
# ESCAPE: Used for pressing the Escape key.
# F1 - F12: Used for pressing the Function keys.

