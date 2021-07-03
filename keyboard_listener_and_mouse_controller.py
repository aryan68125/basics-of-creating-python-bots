from pynput.mouse import Button, Controller

#Make a variable called mouse and set it to an instance of Controller. Now using the mouse variable we can control the mouse.
mouse = Controller()

#Moving the Mouse Relative to Its Position
#mouse.position = (10, 20)

# Click the left button
#mouse.click(Button.left, 1)

#getting mouse position(working)
#for i in range (0,999999999):
#    print ("Current position: " + str(mouse.position))

from pynput import keyboard

def press_callback(key):
    key_pressed = '{}'.format(key)
    print(key_pressed)
    if hasattr(key,'char'):
        if key.char == "z":
            print('Thanks for pressing "z"! That\'s my favorite character!')
    if key == keyboard.Key.esc:
        print('You pressed "escape"! You must want to quit really badly...')


def release_callback(key):
    key_released = '{}'.format(key)
    print(key_released)

l = keyboard.Listener(on_press=press_callback,on_release=release_callback)
l.start()
l.join()