from pynput.keyboard import Controller, Listener
c = Controller()

def press_callback(key):
    if key.char == 'c':
        c.type("ool, dude!")
        return False

l = Listener(on_press=press_callback)
l.start()
l.join()