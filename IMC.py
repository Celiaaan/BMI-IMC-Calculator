class bcolors:
    HEADER = '\033[95m'
    OKCYAN = '\033[96m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ANY = '\033[m'
import os
os.system("color 0b")
os.system("cls")

from datetime import date
now = date.today()

import json
from urllib import request
from urllib.error import HTTPError


def inputint(message):
    while True:
        try:
            userInput = int(input(message))

        except ValueError:
            print("Ce n'est pas un chiffre ! Recommence.")
            continue
        else:
            return userInput
            break


def inputfloat(message):
    while True:
        try:
            userInput = float(input(message))

        except ValueError:
            print("Ce n'est pas un chiffre ! Recommence.")
            continue
        else:
            return userInput
            break

separator = "====================================================="

#######################################################################################################################
#######################################################################################################################


#READY
print(bcolors.OKCYAN + "Bienvenue dans le calculateur de ton indice de masse corporelle (IMC)")
input("Es-tu prêt ? ")
print("Rien à fouttre en vrai...")

#NAME ASKING
name = None                                     #
while not name:
    name = input("Comment t'appelles-tu ? : ")

#HEY
print("Salut, "+name+". Je vais te poser quelques questions.")
print(separator)
#AGE ASKING
age = None
while not age:
    age = inputint("Quel age as-tu ? : ")
age = int(age)
while not (age > 0 and age < 200):
    age = inputint("Tu ne peux pas avoir cet âge là... Quel âge as-tu ? : ")

#YOUR AGE IS
print("Tu as donc " + str(age) + " ans")   #YOUR AGE IS

#HEIGHT ASKING
height = None
while not height:
    height = inputfloat("Quelle taille fais-tu ? (en cm) : ")
height = float(height)
while not (height > 0 and height < 300):
    height = float(inputfloat("Tu ne peux pas avoir cet taille là... Quelle taille fais-tu ? : "))

#WEIGHT ASKING
weight = None
while not weight:
    weight = inputfloat("Et quel poids fais-tu ? (en kg) : ")
weight = float(weight)
while not (weight > 0 and weight < 650):
    weight = float(inputfloat("Tu ne peux pas avoir ce poids là... Quel poids fais-tu ? : "))

height = float(height/100)

# IMC CALC
IMC = float(weight/(height*height))

#RESULT
print(bcolors.BOLD + bcolors.UNDERLINE + "Waw ! Ton IMC est donc : " + bcolors.HEADER + str(IMC))

#RESUME
if IMC >25:
    print("Ton IMC est trop élevé ! (supérieur à 25)")
elif IMC < 18.5:
    print("Ton IMC est trop bas ! (inférieur à 15.5)")
elif 21 < IMC <22:
    print("Ton IMC est parfait ! (entre 21 et 22)")
else:
    print("Ton IMC est dans la norme")


#######################################################################################################################
#######################################################################################################################
#STRINGS FOR THE LOGS
nowtxt = ("Date : " + str(now))
nametxt = ("Nom : " + str(name))
agetxt = ("Age : " + str(age))
IMCtxt = ("IMC : " + str(IMC))


#CREATE THE LOGS FILES
def yes_or_no(question):
    reply = str(input(question+' Oui ou non ? : ')).lower().strip()
    try:
        if reply[0] in ('y','o'):
            return True
        if reply[0] in 'n':
            return False
        else:
            return yes_or_no("J'ai dit OUI ou NON ! : ")
    except:
        return yes_or_no("J'ai dit OUI ou NON ! : ")

log = yes_or_no(bcolors.ANY + bcolors.OKCYAN + "Voulez-vous envoyer le résultat dans logs.txt ? : ")
if log == True:
    txt = open("logs.txt", "a+")
    txt.writelines('\n'.join([separator, nowtxt, nametxt, agetxt, IMCtxt, separator]) + '\n')
else: pass


# La payload
payload = {
    'embeds': [
        {
            'title': 'Imc calc',  # Le titre de la carte
            'description': ('\n'.join([nowtxt, nametxt, agetxt, IMCtxt]) + '\n'),  # Le corps de la carte
            'image': {
            'url': 'https://cdn.discordapp.com/attachments/835949614506573864/844244417867022366/calcul-IMC-indice-de-masse-corporelle-e1587390793294.png'
            }
        },

    ]
}

# Les paramètres d'en-tête de la requête
headers = {
    'Content-Type': 'application/json',
    'user-agent': 'Mozilla/5.0 (X11; U; Linux i686) Gecko/20071127 Firefox/2.0.0.11'
}


def defreq():
    try:
        print(separator)
        print('Un URL de webhook ressemble à ca : https://discord.com/api/webhooks/*****/*****')
        req = request.Request(url=(input("Webhook URL : ")),
                          data=json.dumps(payload).encode('utf-8'),
                          headers=headers,
                          method='POST')
        return req
    except:
        return False


# Puis on l'émet !
def emeq(req):
    if req == False:
        print("Ce n'est pas un URL de webhook !")
        return False
    else:
        try:
            request.urlopen(req)
            print('Webhook correct ! Envoi en cours...')
            return True
        except HTTPError as e:
            print('ERREUR ! Webhook invalide')
            print(e.reason)
            return False
        except:
            print('ERREUR ! Webhook invalide')
            return False




web = yes_or_no(bcolors.OKCYAN + "Voulez-vous envoyer le résultat via discord ? ")

if web == True:
    while emeq(defreq()) == False:
            print("On recommence ! ")

    else:
        pass
else:
    pass





#######################################################################################################################
#END
#######################################################################################################################

input(bcolors.OKCYAN + "Appuie  sur entrée pour terminer ")
print('Au revoir !')

