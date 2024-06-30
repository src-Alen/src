import machine

r = machine.Pin(4, machine.Pin.OUT)
l = machine.Pin(15, machine.Pin.OUT)

l.off()
r.off()