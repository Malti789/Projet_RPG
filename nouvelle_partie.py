"""IMPORTS"""

from tkinter import *
from tkinter import font
import sys, time
import tkinter

"""CONFIGURATION DE LA FENETRE"""

window = Tk()                       #Créer une fenêtre 
window.title("Lighthouse")          #Titre de la fenêtre
window.geometry("1080x720")         #Taille de la fenêtre
""" window.iconbitmap("lighthouse.ico") #Icône de la fenêtre """
window.config(background="black")   #Couleur de fond de la fenêtre

"""FONCTIONS"""

def new():
    player_name = tkinter.Entry()
    player_name.insert
    player_name.pack()

"""CONTENU DE LA FENETRE"""

window.mainloop()