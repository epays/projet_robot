#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from ev3dev.ev3 import *
import os,sys
import time     

mm = ev3.MediumMotor()
assert mm.connected, 'Connecter le medium motor sur port A!'
shot = 0        
while shot <= 4:
        mm.run_to_rel_pos(speed_sp=900, position_sp=(-1080 if direction == 'up' else 1080))
        shot += 1

