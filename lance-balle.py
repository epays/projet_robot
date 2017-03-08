#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from ev3 import MediumMotor()
from ev3dev.ev3 import *
from ev3.ev3dev import InfraredSensor()
from ev3.ev3dev import TouchSensor()
import os, sys
import time     

class RobotTir:
        def __init__(self):
        self.mm = ev3.MediumMotor()
        check(self.mm.connected, 'Connecter le medium motor sur port A!')
  
shot = 0        
    while shot < 4:
        self.mm.run_to_rel_pos(speed_sp=900, position_sp=(-1080 if direction == 'up' else 1080))
        shot = shot +1



