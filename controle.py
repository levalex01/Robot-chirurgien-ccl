import pygame
import serial
import time

# Initialise pygame pour lire les entrées de la manette
pygame.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()

# Ouvre le port série pour communiquer avec l'Arduino
# Remplacez 'COM4' par le nom du port série de votre Arduino
arduino = serial.Serial('COM4', 9600)

angle1 = 90  # Initialise l'angle des servos 1 et 2 à 90 degrés
angle3 = 90  # Initialise l'angle du servo 3 à 90 degrés

while True:
    pygame.event.pump()

    # Si le bouton de flèche haut est enfoncé
    if joystick.get_hat(0)[1] == 1:
        angle1 += 10  # Augmente l'angle des servos 1 et 2 de 10 degrés
        if angle1 > 180:  # Assure que l'angle ne dépasse pas 180 degrés
            angle1 = 180
        arduino.write(('1' + str(angle1)).encode())  # Envoie l'angle aux servos 1 et 2
        time.sleep(1)  # Attend 1 seconde

    # Si le bouton de flèche bas est enfoncé
    if joystick.get_hat(0)[1] == -1:
        angle1 -= 10  # Diminue l'angle des servos 1 et 2 de 10 degrés
        if angle1 < 90:  # Assure que l'angle ne descend pas en dessous de 90 degrés
            angle1 = 90
        arduino.write(('1' + str(angle1)).encode())  # Envoie l'angle aux servos 1 et 2
        time.sleep(1)  # Attend 1 seconde

    # Si le bouton de flèche droite est enfoncé
    if joystick.get_hat(0)[0] == 1:
        angle3 += 10  # Augmente l'angle du servo 3 de 10 degrés
        if angle3 > 180:  # Assure que l'angle ne dépasse pas 180 degrés
            angle3 = 180
        arduino.write(('3' + str(angle3)).encode())  # Envoie l'angle au servo 3
        time.sleep(1)  # Attend 1 seconde

    # Si le bouton de flèche gauche est enfoncé
    if joystick.get_hat(0)[0] == -1:
        angle3 -= 10  # Diminue l'angle du servo 3 de 10 degrés
        if angle3 < 90:  # Assure que l'angle ne descend pas en dessous de 90 degrés
            angle3 = 90
        arduino.write(('3' + str(angle3)).encode())  # Envoie l'angle au servo 3
        time.sleep(1)  # Attend 1 seconde
