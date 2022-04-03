import sys, time

def tw(message):
    for char in message:
        sys.stdout.write(char)          #fonction permettant d'effectuer un typewriter pour chaque texte 
        sys.stdout.flush()              
        time.sleep(0.02) 

"""Pour utiliser cette fonction, commencer par l'importer, puis rappelez la fontion avec un tw(message)"""