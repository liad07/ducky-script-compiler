# Ducky Script Compiler
This is a Python script that can compile and execute Ducky Script. Ducky Script is a simple scripting language used to control the keyboard and mouse of a computer. It is commonly used for automation, penetration testing, and other similar purposes.

## Requirements
- Python 3.x
- PyAutoGUI library
## Usage
1) Save your Ducky Script in a file (e.g. example.ds) in the same directory as the Python script.
2) Open a terminal or command prompt in the directory containing the Python script and the Ducky Script file.
3) Run the following command to execute the script:
``` batch
python ducky_script_compiler.py

```
4) The script will read in the Ducky Script file and execute each command using PyAutoGUI. Supported commands include DELAY, STRING, GUI, ENTER, TAB, SHIFT, ALT, CONTROL, REPEAT, MENU, INSERT, HOME, END, PAGEUP, PAGEDOWN, DELETE, CAPSLOCK, NUMLOCK, SCROLLLOCK, ESCAPE, and F1-F12.
## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please create an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
