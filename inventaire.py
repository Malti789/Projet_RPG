import pygame
import players
import Backend.inventaire as inventaire

class stat:
    def __init__(self):
        self.items=flashlight,battery,pile 

    def inventory(self):
        self.inventory=[items(flashlight,),items(battery)]
        
   compteur=0
   def utilisation(self):
      while compteur <5 :
         if flashlight.used:
            compteur=compteur+1
         else:
            compteur=compteur+7
      if compteur==7:
         compteur=0
      elif battery.used:
            compteur=compteur-1
      else:
            compteur=compteur
    


        