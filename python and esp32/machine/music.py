from machine import Pin, PWM
import time

d = 33
r = 65
m = 131
f = 262
s = 523
l = 1067
x = 2093

p1 =1.25
p2 =0.625
p3 =0.3125

led2 = PWM(Pin(4))
led2.duty(512)

led2.freq(r)
time.sleep(p3)
led2.freq(d)
time.sleep(p3)
led2.freq(r)
time.sleep(p2)
led2.freq(d)
time.sleep(p3)
led2.freq(r)
time.sleep(p2)
led2.freq(m)
time.sleep(p2)
led2.freq(s)
time.sleep(p2)
led2.freq(m)
time.sleep(p2)

led2.freq(1)

    
        


