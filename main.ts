input.onButtonPressed(Button.A, function () {
    led.unplot(Xpos, Ypos)
    Xpos += -1
    led.plot(Xpos, Ypos)
    if (Xpos == -1) {
        Xpos = 4
    }
})
input.onButtonPressed(Button.AB, function () {
    xgunpos = Xpos
    ygunpos = 3
    while (true) {
        led.plot(xgunpos, ygunpos)
        basic.pause(100)
        led.unplot(xgunpos, ygunpos)
        ygunpos += -1
        if (ygunpos == -1) {
            break;
        }
    }
})
input.onButtonPressed(Button.B, function () {
    led.unplot(Xpos, Ypos)
    Xpos += 1
    led.plot(Xpos, Ypos)
    if (Xpos == 5) {
        Xpos = 0
    }
})
let ygunpos = 0
let xgunpos = 0
let Xpos = 0
let Ypos = 0
Ypos = 4
Xpos = 2
basic.forever(function () {
    led.plot(Xpos, Ypos)
})
