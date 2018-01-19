#!/usr/bin/env python
# coding: utf-8

import datetime
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import urllib
import re
import sys
import os
import requests
import smtplib

# ------ Parametre ------ #
#Adresse d'envoi (pour gmail desactiver la double authentification (recréer un compte est une solution))
fromaddr = ''
mdp = ''
#Destinataire(s) éventuellement plusieurs separés par des virgules
toaddr = ''
#Fichier txt contenant la derniere monnaie actuelle
chemin_absolu_vers_fichier = ''

smtp = ''
port =
subject = ''
text_mail = ''
# ----------------------- #



# ------ Algorithme ------ #

# Pour recuperer la derniere crypto currency de binance
page = urllib.urlopen('https://support.binance.com/hc/en-us/sections/115000106672-New-Listings')
strpage = str(page.read())
strpage = strpage[5800 : 8800]
strpage = strpage.replace(' ', '')

derniere_ico = str('')
match1 = re.search(r'\(', strpage)
match2 = re.search(r'\)', strpage)

debut = 1
fin = match2.start() - match1.start()
while debut < fin:
    derniere_ico += strpage[match1.start()+debut]
    debut+=1

date = datetime.datetime.now()
print("Derniere monnaie en date: "+derniere_ico+" a "+str(date.strftime("%H:%M:%S")+" le "+date.strftime("%d %b %Y")))


# Verifie ce qu'on a dans le fichier pour voir si il y a eu une mise à jour
mon_fichier = open(chemin_absolu_vers_fichier, "r")
contenu = mon_fichier.read()
mon_fichier.close()
mon_fichier = open(chemin_absolu_vers_fichier, "w")
#Verifie si on est à jour
if (contenu != derniere_ico):
    mon_fichier.write(derniere_ico)
    print("Mise à jour")

    #Création du mail
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = subject
    body = text_mail
    msg.attach(MIMEText(body, 'plain'))

    #Envoi du mail
    server = smtplib.SMTP(smtp, port)
    server.starttls()
    server.login(fromaddr, mdp)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

else:
    mon_fichier.write(derniere_ico)
    print("Deja à jour")

mon_fichier.close()
# ----------------------- #
