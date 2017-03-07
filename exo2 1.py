#!/usr/bin/env python3
import * from ev3dev.ev3 
import sleep from time       
import sys

def beeps( nb ):  #plusieurs bips
   for i in range (0,nb):
      Sound.beep()
      sleep(.2)

def exitrouge():
   if cl.value(0) > 100:  # panneau rouge 
      if cl.value(1) + cl.value(2) < 50:
         m1.run_forever(speed_sp = 0)
         m2.run_forever(speed_sp = 0)
         beeps(3)
         sleep(1)
         sys.exit(0)

m1 = LargeMotor('outB')
assert m1.connected, "Connecter un large motor sur outB"
m2 = LargeMotor('outC')
assert m2.connected, "Connecter un large motor sur outC"

beeps(1)

ir = InfraredSensor()
assert ir.connected, "Connecter le senseur infrarouge a un des ports"

#Mettre le senseur infrarouge en mode de proximite
ir.mode = 'IR-PROX'

cl = ColorSensor() 
assert cl.connected, "Connecter le senseur de couleur a un des ports"

# Mettre le senseur en mode RGB
cl.mode='RGB-RAW'

cur_distance = ir.value()
# print "Distance %d cur_distance de depart" % cur_distance

m1.run_forever(speed_sp = 0)
m2.run_forever(speed_sp = 0)

while ir.value() > 2:
    exitrouge()  #stoppe avec panneau rouge

    cur_distance = ir.value()
    # print "Distance1 %d cur_distance" % cur_distance

    while ir.value() > 7:
       exitrouge()

       cur_distance = ir.value()
       # print "Distance2 %d cur_distance" % cur_distance
       m1.run_forever(speed_sp = 300 - 2000/(cur_distance + 3))
       m2.run_forever(speed_sp = 300 - 2000/(cur_distance + 3))

    m1.run_forever(speed_sp = 0)
    m2.run_forever(speed_sp = 0)
    m1.run_forever(speed_sp = -400)
    m2.run_forever(speed_sp = -400)
    sleep(1.5)

    exitrouge()  #stoppe avec panneau rouge

    for num in range(1,5):
        m2.run_timed(speed_sp=400)
        sleep(0.6)
        exitrouge()  #stoppe avec panneau rouge

        if ir.value() < 7:
            break

m1.run_forever(speed_sp = 0)
m2.run_forever(speed_sp = 0)

beeps(2)
sleep(1)