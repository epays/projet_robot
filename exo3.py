import LargeMotor  from ev3.lego 
import * from ev3dev.ev3 
import InfraredSensor from ev3.lego 

obs_detection = InfraredSensor()

distance = 30
gauche = LargeMotor(port=LargeMotor.PORT.B)
droite = LargeMotor(port=LargeMotor.PORT.C)

if obs_detection <= distance:
            gauche.stop()
            droite.stop()








