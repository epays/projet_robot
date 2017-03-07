import ev3dev.ev3 as ev3
from ev3 import LargeMotor 
from ev3dev.ev3 import *
from ev3.ev3dev import InfraredSensor()
import os, sys
obs_detection = ev3.InfraredSensor()
obs_detection.mode = 'IR-DIST-CM'
distance = 30

m1 = ev3.LargeMotor('outB')
assert m1.connected, "Connecter un large motor sur outB"
m2 = ev3.LargeMotor('outC')
assert m2.connected, "Connecter un large motor sur outC"

m1.run_forever(speed_sp=500)
m2.run_forever(speed_sp=500)

if obs_detection.value <= distance:
            m1.stop()
            m2.stop()









