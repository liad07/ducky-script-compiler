import pyautogui
import time
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from ttkthemes import ThemedStyle

root = tk.Tk()
root.geometry("500x500")
root.configure(bg="#2b2b2b")


# Define functions
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
        for i in range(times - 1):
            linesof = result.split("\n")
            print(len(linesof))
            for j in range(len(linesof)):
                runer(linesof[j].split(" ")[0],
                      linesof[j].replace(linesof[j].split(" ")[0].strip(), "").strip().replace(" ", ""))

    if comand == "KNOWN":
        text_widget.tag_config("orange", foreground="orange")
        start = "1.0"
        while True:
            start = text_widget.search(comand, start, stopindex="end")
            if not start:
                break
            end = f"{start}+{len(comand)}c"
            text_widget.tag_add("orange", start, end)
            start = end


def run_script():
    global lines
    global script_text
    script = script_text.get("1.0", "end-1c")
    lines = script.split("\n")

    for i in range(len(lines)):
        comand = lines[i].split(" ")[0]
        z = lines[i].split(" ")
        runer(comand, z)


def open_file():
    global script_text
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, "r") as f:
            script_text.delete("1.0", tk.END)
            script_text.insert(tk.END, f.read())


def save_file():
    global script_text
    file_path = filedialog.asksaveasfilename(defaultextension=".ds", filetypes=[("Ducky Script files", "*.ds")])
    if file_path:
        with open(file_path, "w") as f:
            f.write(script_text.get("1.0", "end-1c"))


def clear_script():
    global script_text
    script_text.delete("1.0", tk.END)
# Create GUI
root.title("Ducky Script Compiler")
# Create GUI (continued)
style = ThemedStyle(root)
style.set_theme("equilux")

title_label = ttk.Label(root, text="Ducky Script Compiler", font=("Helvetica", 20))
title_label.pack(pady=10)

script_frame = ttk.Frame(root)
script_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

script_scrollbar = ttk.Scrollbar(script_frame)
script_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

script_text = tk.Text(script_frame, wrap=tk.NONE, yscrollcommand=script_scrollbar.set, bg="#2b2b2b", fg="#fff",
                      insertbackground="#fff")
script_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

script_scrollbar.config(command=script_text.yview)

open_button = ttk.Button(root, text="Open File", command=open_file)
open_button.pack(side=tk.LEFT, padx=20)
open_button = ttk.Button(root, text="save File", command=save_file)
open_button.pack(side=tk.LEFT, padx=20)

run_button = ttk.Button(root, text="Run Script", command=run_script)
run_button.pack(side=tk.RIGHT, padx=20)

root.mainloop()
