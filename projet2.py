import random

nombre = random.randint(1, 100)
nbrsuppose = None

while nbrsuppose != nombre:
    nbrsuppose = int(input("Choisir un nombre entre 1 et 100: "))
    
    if nbrsuppose > nombre:
        print("Trop élevé !")
    elif nbrsuppose < nombre:
        print("Trop bas !")
    else:
        print("Correcte !")


