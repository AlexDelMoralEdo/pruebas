from pynput.keyboard import Key, Controller
import time

Keyboard = Controller()

time.sleep(5)
while True:
    for letter in "Donde estasDonde estas":
        Keyboard.press(letter)
        Keyboard.release(letter)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    time.sleep(0.2)
