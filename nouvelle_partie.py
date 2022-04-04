"""IMPORTS"""

from tkinter import *
from tkinter import font
import sys, time
import tkinter

"""CONFIGURATION DE LA FENETRE"""

window = Tk()                       #Créer une fenêtre 
window.title("Lighthouse")          #Titre de la fenêtre
window.geometry("1080x720")         #Taille de la fenêtre
window.config(background="black")   #Couleur de fond de la fenêtre

"""FONCTIONS"""

def new():
    player_name = tkinter.Entry()
    player_name.insert
    player_name.pack()

"""CONTENU DE LA FENETRE"""

bouton_nouvelle_partie= Button(window, text="Nouvelle Partie")
bouton_nouvelle_partie.pack()

bouton_charger_partie= Button(window, text="Charger Partie")
bouton_charger_partie.pack()

bouton_credits= Button(window, text="Crédits")
bouton_credits.pack()

bouton_quitter= Button(window, text="Quitter", command=window.quit)
bouton_quitter.pack()

""""""

window.mainloop()
