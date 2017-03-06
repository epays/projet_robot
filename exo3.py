#!/usr/bin/env python3
from ev3dev.ev3 import *
from ev3.lego import InfraredSensor
class ev3dev.core.InfraredSensor

obs_detection = InfraredSensor()

gauche = LargeMotor(port=LargeMotor.PORT.B)
droite = LargeMotor(port=LargeMotor.PORT.C)

if obs_detection <= distance:
            gauche.stop()
            droite.stop()







