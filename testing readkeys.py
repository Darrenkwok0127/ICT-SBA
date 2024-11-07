from readchar import readkey, key
while True:
    k = readkey()
    if k == "a":
        print("a")
    elif k == key.ENTER:
        print("ENTER Pressed")
    elif k == key.UP:
        print("UP Pressed")
    elif k == key.DOWN:
        print("DOWN Pressed")
    elif k == key.LEFT:
        print("LEFT Pressed")
    elif k == key.RIGHT:
        print("RIGHT Pressed")
    elif k == key.ESC:
        break

