#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from ev3 import MediumMotor
from ev3 import LargeMotor
from ev3dev.ev3 import *
from ev3.ev3dev import InfraredSensor
from ev3.ev3dev import TouchSensor
import os, sys
import time, random

obs_detection = ev3.InfraredSensor()
obs_detection.mode = 'IR-PROX'


class RobotPls:
    def __init__(self):
        self.lm = ev3.LargeMotor()
        self.rm = ev3.LargeMotor()
        self.mm = ev3.MediumMotor()
        self.ir = ev3.InfraredSensor()

        check(self.lm.connected, 'Connecter le large motor gauche sur port B !')
        check(self.rm.connected, 'Connecter le large motor droit sur port C !')
        check(self.mm.connected, 'Connecter le medium motor sur port A!')
        check(self.ir.connected, 'Connecter le Infrared Sensor !')


    while obs_detection.value >= 30:
        self.lm.run_forever(speed_sp=500)
        self.rm.run_forever(speed_sp=500)     
shot = 0        
    while obs_detection.value <= 30 && shot < 4:
        self.lm.stop()
        self.rm.stop()
        self.mm.run_to_rel_pos(speed_sp=900, position_sp=(-1080 if direction == 'up' else 1080))
        shot = shot +1
        
