from classes.trades import TradeResource
from classes.game import Game

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
    Troc("Marchant de ballon",TradeResource(1, items[1]),TradeResource(2, items[0]), True)
    Troc("Marchant de ballon",TradeResource(1, items[2]),TradeResource(5, items[3]), True)
    Troc("Marchant de ballon",TradeResource(1, items[4]),TradeResource(2, items[5]), True)
    Troc("Marchant de ballon",TradeResource(1, items[6]),TradeResource(14, items[7]), True)
    Troc("Marchant de ballon",TradeResource(1, items[8]),TradeResource(3, items[9]), True)
    Troc("Marchant de ballon",TradeResource(1, items[11]),TradeResource(2, items[12]), True)
    Troc("Marchant de ballon",TradeResource(1, items[13]),TradeResource(4, items[14]), True)

    #Vendeuse d'armures
    Troc("Vendeuse d'armures",TradeResource( 1, items[15]),TradeResource(1, items[0]), True)
    Troc("Vendeuse d'armures",TradeResource( 1, items[4]),TradeResource(4, items[7]), True)
    Troc("Vendeuse d'armures",TradeResource( 1, items[16]),TradeResource(4, items[17]), True)
    Troc("Vendeuse d'armures",TradeResource( 1, items[18]),TradeResource(22, items[3]), True)
    Troc("Vendeuse d'armures",TradeResource( 1, items[19]),TradeResource(4, items[22]), True)
    Troc("Vendeuse d'armures",TradeResource( 1, items[12]),TradeResource(3, items[20]), True)
    Troc("Vendeuse d'armures",TradeResource( 1, items[21]),TradeResource(2, items[13]), True)

    #Forgeronne des Tarides
    Troc("Forgeronne des Tarides",TradeResource( 1, items[3]),TradeResource(2, items[0]), True)
    Troc("Forgeronne des Tarides",TradeResource( 1, items[10]),TradeResourceTradeResource(5, items[5]), True)
    Troc("Forgeronne des Tarides",TradeResource( 1, items[23]),TradeResource(8, items[19]), True)
    Troc("Forgeronne des Tarides",TradeResource( 1, items[8]),TradeResource(1, items[25]), True)
    Troc("Forgeronne des Tarides",TradeResource( 1, items[22]),TradeResourceTradeResource(5, items[4]), True)
    Troc("Forgeronne des Tarides",TradeResource( 1, items[26]),TradeResource(4, items[27]), True)
    Troc("Forgeronne des Tarides",TradeResource( 1, items[28]),TradeResourceTradeResource(5, items[29]), True)

    #Alchimiste de Sombre-Comté
    Troc("Alchimiste de Sombre-Comté",TradeResource( 1, items[3]),TradeResource(2, items[0]), True)
    Troc("Alchimiste de Sombre-Comté",TradeResource( 1, items[10]),TradeResourceTradeResource(5, items[5]), True)
    Troc("Alchimiste de Sombre-Comté",TradeResource( 1, items[23]),TradeResource(8, items[19]), True)
    Troc("Alchimiste de Sombre-Comté",TradeResource( 1, items[8]),TradeResource(1, items[25]), True)
    Troc("Alchimiste de Sombre-Comté",TradeResource( 1, items[22]),TradeResourceTradeResource(5, items[4]), True)
    Troc("Alchimiste de Sombre-Comté",TradeResource( 1, items[26]),TradeResource(4, items[27]), True)
    Troc("Alchimiste de Sombre-Comté",TradeResource( 1, items[28]),TradeResourceTradeResource(5, items[29]), True)

    startGame = Game(1, 2)
