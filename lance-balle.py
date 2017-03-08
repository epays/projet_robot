#!/usr/bin/env python3
import ev3dev.ev3 as ev3
from ev3 import MediumMotor()
from ev3dev.ev3 import *
from ev3.ev3dev import InfraredSensor()
from ev3.ev3dev import TouchSensor()
import os, sys
import time





        # Connecte les équipements nécessaires et on vérifie
class Patator:
    def __init__(self):
        self.mm = ev3.MediumMotor()
        self.ir = ev3.InfraredSensor()
        self.ts = ev3.TouchSensor()

        check(self.mm.connected, 'Connecter le medium motor !')

        check(self.ir.connected, 'Connecter le Infrared Sensor !')
        check(self.ts.connected, 'Connecter le touch sensor !')

        # Reset des moteurs
        for m in (self.ir, self.ts, self.mm):
            m.reset()
            m.position = 0
            m.stop_action = 'brake'

       

    class Shooter(TRACK3R):

    def __init__(self, medium_motor=OUTPUT_A):
        TRACK3R.__init__(self, medium_motor)
        self.remote.on_beacon = self.fire_ball

    def fire_ball(self, state):
        if state:
            self.medium_motor.run_to_rel_pos(speed_sp=400, position_sp=3*360)
        else:
self.medium_motor.stop()



