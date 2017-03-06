#! / usr / bin / env python3 
import ev3dev.ev3 as ev3
from ev3dev.ev3  import  *
# coding: utf-8


cl = colorSENSOR () #définir le capteur comme capteur de couleur
assert cl.connected, "Connecter un capteur de couleur à un port de capteur" #vérifier que le capteur est connecté sinon erreur
cl.mode = 'COL-COLOR' #mettre le capteur cl en mode reconnaissance de couleur
colors = ( 'inconnu', 'noir', 'bleu', 'vert', 'jaune', 'rouge', 'blanc', 'marron', lang='fr')
if colors = "rouge":
	Sound.speak('Au Revoir', lang='fr').exit() #si la couleur est rouge, le programme s'arrête
	pass
else :
	print(colors[cl.value()]) #affiche la couleur en chaine de caractère
    Sound.speak(colors[cl.value()]).wait() #dit la couleur
