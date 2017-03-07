#! / usr / bin / env python3 
import ev3dev.ev3 as ev3
import  * from ev3dev.ev3  

ev3.Sound.setLanguage("French") #définir la langue sur français


cl = colorSENSOR () #définir le capteur comme capteur de couleur
assert cl.connected, "Connecter un capteur de couleur à un port de capteur" #vérifier que le capteur est connecté sinon erreur
cl.mode = 'COL-COLOR' #mettre le capteur cl en mode reconnaissance de couleur
colors = ( "inconnu", "noir", "bleu", "vert", "vert", "rouge", "blanc", "marron")
if colors = "rouge":
	ev3.Sound.speak('Au Revoir').exit() #si la couleur est rouge, le programme s'arrête
	pass
else :
	print(colors[cl.value()]) #affiche la couleur en chaine de caractère
    Sound.speak(colors[cl.value()]).wait() #dit la couleur
