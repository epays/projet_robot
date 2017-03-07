#! / usr / bin / env python3 
import ev3dev.ev3 as ev3
from ev3dev.ev3  import  *
from time import sleep
import sys
coding : utf-8

cl = colorSensor () #définir le capteur comme capteur de couleur
assert cl.connected, "Connecter un capteur de couleur à un port de capteur" #vérifier que le capteur est connecté sinon erreur
cl.mode = 'COL-COLOR' #mettre le capteur cl en mode reconnaissance de couleur
colors = ( 'inconnu', 'noir', 'bleu', 'vert', 'jaune', 'Au Revoir !', 'blanc', 'marron')
while cl.value() != 5:
	Sound.speak(colors[cl.value()]).wait() #tant que la couleur est différente de rouge, le programme dicte les couleurs qu'il voit
	sleep(2)
if cl.value() == 5:
	Sound.speak(colors[cl.value()]).wait() #si la couleur est rouge, le programme s'arrête
