import LargeMotor  as ev3 
import ev3dev.ev3 as ev3 
 import * as ev3
import ev3.InfraredSensor() as ev3
import os, sys

mot1 = ev3.LargeMotor('outB')
assert m1.connected, "Connecter un large motor sur outB"
mot2 = ev3.LargeMotor('outC')
assert m2.connected, "Connecter un large motor sur outC"

mot1.run_timed(time_sp=3000, speed_sp=500)
mot2.run_timed(time_sp=3000, speed_sp=500)

obs_detection = ev3.InfraredSensor()

distance = 30


if obs_detection <= distance:
            mot1.stop()
            mot2.stop()









