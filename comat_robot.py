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
obs_detection.mode = 'IR-DIST-CM'
distance = 30

class robotPls:
    def __init__(self):
        self.lm = ev3.LargeMotor()
        self.rm = ev3.MediumMotor()
        self.mm = ev3.MediumMotor()
        self.ir = ev3.InfraredSensor()
        self.ts = ev3.TouchSensor()

        check(self.lm.connected, 'Connecter le large motor gauche !')
        check(self.rm.connected, 'Connecter le large motor droit !')
        check(self.mm.connected, 'Connecter le medium motor !')
        check(self.ir.connected, 'Connecter le Infrared Sensor !')
        check(self.ts.connected, 'Connecter le touch sensor !')

        # Reset des moteurs
        for m in (self.ir, self.ts, self.mm, self.lm, self.rm):
            m.reset()
            m.position = 0
            m.stop_action = 'brake'




while obs_detection.value >= distance:
    lm.run_forever(speed_sp=500)
    rm.run_forever(speed_sp=500)
else      
    def shoot(self, direction='up'):
           
       # Lance une balle
       self.mm.run_to_rel_pos(speed_sp=900, position_sp=(-1080 if direction == 'up' else 1080))
    while 'running' in self.mm.state:
            time.sleep(0.1)



    def shoot(direction):
    def on_press(state):
            if state: self.shoot(direction)
    return 0
