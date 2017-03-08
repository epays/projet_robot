#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from ev3 import MediumMotor
from ev3 import LargeMotor
from ev3dev.ev3 import *
from ev3dev.ev3 import InfraredSensor
from ev3dev.ev3 import TouchSensor
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




    while obs_detection.value >= 30:
        lm.run_forever(speed_sp=500)
        rm.run_forever(speed_sp=500)     
shot = 0        
    while obs_detection.value <= 30 && shot < 4:
        lm.stop()
        rm.stop()
        mm.run_to_rel_pos(speed_sp=900, position_sp=(-1080 if direction == 'up' else 1080))
        shot = shot +1
        
