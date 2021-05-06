import Troc

items = [
        #0
        "PO", "Potion de soins", "Coupe dorée", "Hache courte", "Médaillon de jade",
        #5
        "Bandage en lin", "Masse de l'Alliance", "Cheddar de Hurlevent", "Breuvage des anges", "Jolie pourpée",
        #10
        "Jolie pourpée", "Dague gilnéenne", "Gemme ténébreuse", "Sifflet de familier fidele", "Elexir de vigueur",
        #15
        "Dage en fer", "Coupe Dorée", "Potion de soins", "Couronne de rubis", "Sphère de sagesse",
        #20
        "Bouclier gnome", "Baguette en saphir", "Potion de nuit", "Parchemin Arcanique", "Très jolie chapeau",
        #25
        "Cristal en colère", "Bougie semperadente", "Canne à peche gobeline", "Amulette du tigre", "Flûte captivante"
    ]

if __name__ == "__main__":

    #Marchant de ballon
    Troc((1, items[1]),(2, items[0]), True, "Marchant de ballon")
    Troc((1, items[2]),(5, items[3]), True, "Marchant de ballon")
    Troc((1, items[4]),(2, items[5]), True, "Marchant de ballon")
    Troc((1, items[6]),(14, items[7]), True, "Marchant de ballon")
    Troc((1, items[8]),(3, items[9]), True, "Marchant de ballon")
    Troc((1, items[11]),(2, items[12]), True, "Marchant de ballon")
    Troc((1, items[13]),(4, items[14]), True, "Marchant de ballon")

    #Vendeuse d'armures
    Troc((1, items[15]),(1, items[0]), True, "Vendeuse d'armures")
    Troc((1, items[4]),(4, items[7]), True, "Vendeuse d'armures")
    Troc((1, items[16]),(4, items[17]), True, "Vendeuse d'armures")
    Troc((1, items[18]),(22, items[3]), True, "Vendeuse d'armures")
    Troc((1, items[19]),(4, items[22]), True, "Vendeuse d'armures")
    Troc((1, items[12]),(3, items[20]), True, "Vendeuse d'armures")
    Troc((1, items[21]),(2, items[13]), True, "Vendeuse d'armures")

    #Forgeronne des Tarides
    Troc((1, items[3]),(2, items[0]), True, "Forgeronne des Tarides")
    Troc((1, items[10]),(5, items[5]), True, "Forgeronne des Tarides")
    Troc((1, items[23]),(8, items[19]), True, "Forgeronne des Tarides")
    Troc((1, items[8]),(1, items[25]), True, "Forgeronne des Tarides")
    Troc((1, items[22]),(5, items[4]), True, "Forgeronne des Tarides")
    Troc((1, items[26]),(4, items[27]), True, "Forgeronne des Tarides")
    Troc((1, items[28]),(5, items[29]), True, "Forgeronne des Tarides")

