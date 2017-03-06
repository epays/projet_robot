from ev3  import LargeMotor  
from ev3dev  import * 
from ev3 import *
from ev3 import InfraredSensor 

moteur = Motor(OUTPUT_A)
moteur.run_timed(time_sp=3000, speed_sp=500)
obs_detection = InfraredSensor()

distance = 30
gauche = LargeMotor(port=LargeMotor.PORT.B)
droite = LargeMotor(port=LargeMotor.PORT.C)

if obs_detection <= distance:
            gauche.stop()
            droite.stop()








