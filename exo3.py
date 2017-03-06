from ev3  import LargeMotor  
from ev3dev  import * 
from ev3 import *
from ev3 import InfraredSensor() 

mot1 = LargeMotor('outB')
assert m1.connected, "Connecter un large motor sur outB"
mot2 = LargeMotor('outC')
assert m2.connected, "Connecter un large motor sur outC"

mot1.run_timed(time_sp=3000, speed_sp=500)
mot2.run_timed(time_sp=3000, speed_sp=500)

obs_detection = InfraredSensor()

distance = 30


if obs_detection <= distance:
            mot1.stop()
            mot2.stop()
else
pass








