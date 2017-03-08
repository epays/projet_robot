#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
import os, sys
import time, random

obs_detection = ev3.InfraredSensor()
obs_detection.mode = 'IR-PROX'

lm = ev3.LargeMotor('outB')
assert lm.connected, "Connecter un large motor sur outB"
rm = ev3.LargeMotor('outC')
assert rm.connected, "Connecter un large motor sur outC"
mm = ev3.MediumMotor('outA')
assert mm.connected, "Connecter un medium motor sur outA"
ir = ev3.InfraredSensor('outD')
assert ir.connected, "Connecter un infrared sensor sur outD"

shot = 0

while obs_detection.value >= 30:
        lm.run_forever(speed_sp=500)
        rm.run_forever(speed_sp=500) 
        
while obs_detection.value <= 30 and shot < 4:
        lm.stop()
        rm.stop()
        mm.run_to_rel_pos(speed_sp=900, position_sp=(-1080 if direction == 'up' else 1080))
        shot += 1
