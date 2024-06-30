from machine import Pin, PWM
import time


led2 = PWM(Pin(15))
led2.freq(2000)


while True:
    for i in range(0, 1024):
        led2.duty(i)

    for i in range(1023, -1, -1):
        led2.duty(i)
