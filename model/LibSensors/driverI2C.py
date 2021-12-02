# coding: utf-8
import smbus
import time
import sys
import tty

bus = smbus.SMBus(1)  # pour I2C-1 (0 pour I2C-0)

# Indiquez ici les deux adresses de l'ecran LCD
# celle pour les couleurs du fond d'ecran 
# et celle pour afficher des caracteres
DISPLAY_RGB_ADDR = 0x62
DISPLAY_TEXT_ADDR = 0x3e

# Completez le code de la fonction permettant de choisir la couleur
# du fond d'ecran, n'oubliez pas d'initialiser l'ecran
def setRGB(rouge,vert,bleu):
	# rouge, vert et bleu sont les composantes de la couleur qu'on vous demande
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x00,0x00)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x01,0x00)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x02,bleu)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x03,vert)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x04,rouge)
	bus.write_byte_data(DISPLAY_RGB_ADDR,0x08,0xAA)
	print("Couleur écran changée")

# Envoie  a l'ecran une commande concerant l'affichage des caracteres
# (cette fonction vous est donnes gratuitement si vous
# l'utilisez dans la fonction suivante, sinon donnez 2000€
# a la banque et allez dictement en prison :)
def textCmd(cmd):
    bus.write_byte_data(DISPLAY_TEXT_ADDR,0x80,cmd)

# Completez le code de la fonction permettant d'ecrire le texte recu en parametre
# Si le texte contient un \n ou plus de 16 caracteres pensez a gerer
# le retour a la ligne
def setText(texte):
	textCmd(0x01)
	time.sleep(.1)
	textCmd(0x0F)
	time.sleep(.1)
	textCmd(0x38)
	time.sleep(.1)
	i = 0
	cpt = 0
	for c in texte:
	# pour un caractere c a afficher :
		bus.write_byte_data(DISPLAY_TEXT_ADDR,0x40,ord(c))
		time.sleep(0.2)
	# ...
		if ((i > 14) or (c == "\n")):   # si on rencontre \n ou si on depasse 16 caracteres
			textCmd(0xc0) # pour passer a la ligne
			i = 0
		i=i+1
		cpt=cpt+1
		if (cpt==31):
			textCmd(0x01)
			textCmd(0x0F)
			textCmd(0x38)
			cpt=0
			i=0
	# ...
	print ("texte ecrit")

def setColor(texte):
	if (texte=="blanc"):
		setRGB(255,255,255)
	if (texte=="vert"):
		setRGB(97, 255, 0)
	if (texte=="violet"):
		setRGB(97, 12, 255)

def echoing():
	while True:
		tty.setraw(sys.stdin.fileno())
		c=sys.stdin.read(1)
		setText(c)
