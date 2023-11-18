def on_button_pressed_a():
    global Xpos
    led.unplot(Xpos, Ypos)
    Xpos += -1
    led.plot(Xpos, Ypos)
    if Xpos == -1:
        Xpos = 4
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global xgunpos, ygunpos
    xgunpos = Xpos
    ygunpos = 3
    while True:
        led.plot(xgunpos, ygunpos)
        basic.pause(100)
        led.unplot(xgunpos, ygunpos)
        ygunpos += -1
        if ygunpos == -1:
            break
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global Xpos
    led.unplot(Xpos, Ypos)
    Xpos += 1
    led.plot(Xpos, Ypos)
    if Xpos == 5:
        Xpos = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

ygunpos = 0
xgunpos = 0
Xpos = 0
Ypos = 0
Ypos = 4
Xpos = 2

def on_forever():
    led.plot(Xpos, Ypos)
basic.forever(on_forever)
