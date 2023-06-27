import keyboard
import string


def getkey():
    for c in string.ascii_lowercase:
        if keyboard.is_pressed(c):
            return ord(c)
    return 0
