#!/usr/bin/env python3				
from ev3dev.ev3 import *
import ev3dev.ev3 as ev3
from time import sleep
import sys

m1 = ev3.LargeMotor('outB')
assert m1.connected, "Connecter un large motor sur outB"
m2 = ev3.LargeMotor('outC')
assert m2.connected, "Connecter un large motor sur outC"

ir = InfraredSensor()
assert ir.connected, "Connecter svp le senseur infrarouge a un des ports"

#Mettre le senseur infrarouge en mode de proximite
ir.mode = 'IR-PROX'


m1.run_forever(speed_sp = 400) #Les moteurs avancent en permanence
m2.run_forever(speed_sp = 400)

cur_distance = 1000

while cur_distance >= 0:
	cur_distance = ir.value()

	if cur_distance <= 40: #Si la distance entre lobstacle et la machine est inférieure ou égale à 40
		m1.stop() #Les moteurs s'arrêtent
		m2.stop()
		m1.run_timed(time_sp=2000, speed_sp=-400)
		m2.run_timed(time_sp=2000, speed_sp=-400)
		sleep(3)
		m1.run_to_rel_pos(position_sp=45, speed_sp=400, stop_action="hold") # Le moteur 1 tourne à 45 degrées
		sleep(3)
		m1.run_forever(speed_sp = 400)
		m2.run_forever(speed_sp = 400)
	else:
		m1.run_forever(speed_sp = 400)
		m2.run_forever(speed_sp = 400)
