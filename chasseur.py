from classes.trades import TradeResource
from classes.trades import Troc
from classes.game import GameManager
from classes.game import Game

items = [
        #0
        "PO", "Potion de soins", "Coupe dorée", "Hache courte", "Médaillon de jade",
        #5
        "Bandage en lin", "Masse de l'Alliance", "Cheddar de Hurlevent", "Breuvage des anges", "Jolie pourpée",
        #10
        "Jolie pourpée", "Dague gilnéenne", "Gemme ténébreuse", "Sifflet de familier fidele", "Elexir de vigueur",
        #15
        "Dague en fer", "Coupe Dorée", "Potion de soins", "Couronne de rubis", "Sphère de sagesse",
        #20
        "Bouclier gnome", "Baguette en saphir", "Potion de nuit", "Parchemin Arcanique", "Très jolie chapeau",
        #25
        "Cristal en colère", "Bougie semperadente", "Canne à peche gobeline", "Amulette du tigre", "Flûte captivante"
    ]

if __name__ == "__main__":
    hand = [
        TradeResource(10, "PO"),
    ]

    trades = []

    #Marchant de ballon
    trades.append(Troc("Marchant de ballon",TradeResource(1, items[1]),TradeResource(2, items[0]), True))
    trades.append(Troc("Marchant de ballon",TradeResource(1, items[2]),TradeResource(5, items[3]), True))
    trades.append(Troc("Marchant de ballon",TradeResource(1, items[4]),TradeResource(2, items[5]), True))
    trades.append(Troc("Marchant de ballon",TradeResource(1, items[6]),TradeResource(14, items[7]), True))
    trades.append(Troc("Marchant de ballon",TradeResource(1, items[8]),TradeResource(3, items[9]), True))
    trades.append(Troc("Marchant de ballon",TradeResource(1, items[11]),TradeResource(2, items[12]), True))
    trades.append(Troc("Marchant de ballon",TradeResource(1, items[13]),TradeResource(4, items[14]), True))

    #Vendeuse d'armures
    trades.append(Troc("Vendeuse d'armures",TradeResource( 1, items[15]),TradeResource(1, items[0]), True))
    trades.append(Troc("Vendeuse d'armures",TradeResource( 1, items[4]),TradeResource(4, items[7]), True))
    trades.append(Troc("Vendeuse d'armures",TradeResource( 1, items[16]),TradeResource(4, items[17]), True))
    trades.append(Troc("Vendeuse d'armures",TradeResource( 1, items[18]),TradeResource(22, items[3]), True))
    trades.append(Troc("Vendeuse d'armures",TradeResource( 1, items[19]),TradeResource(4, items[22]), True))
    trades.append(Troc("Vendeuse d'armures",TradeResource( 1, items[12]),TradeResource(3, items[20]), True))
    trades.append(Troc("Vendeuse d'armures",TradeResource( 1, items[21]),TradeResource(2, items[13]), True))

    #Forgeronne des Tarides
    trades.append(Troc("Forgeronne des Tarides",TradeResource( 1, items[3]),TradeResource(2, items[0]), True))
    trades.append(Troc("Forgeronne des Tarides",TradeResource( 1, items[10]),TradeResource(5, items[5]), True))
    trades.append(Troc("Forgeronne des Tarides",TradeResource( 1, items[23]),TradeResource(8, items[19]), True))
    trades.append(Troc("Forgeronne des Tarides",TradeResource( 1, items[8]),TradeResource(1, items[25]), True))
    trades.append(Troc("Forgeronne des Tarides",TradeResource( 1, items[22]),TradeResource(5, items[4]), True))
    trades.append(Troc("Forgeronne des Tarides",TradeResource( 1, items[26]),TradeResource(4, items[27]), True))
    trades.append(Troc("Forgeronne des Tarides",TradeResource( 1, items[28]),TradeResource(5, items[29]), True))

    #Alchimiste de Sombre-Comté
    trades.append(Troc("Alchimiste de Sombre-Comté",TradeResource( 1, items[29]),TradeResource(2, items[0]), True))
    trades.append(Troc("Alchimiste de Sombre-Comté",TradeResource( 1, items[5]),TradeResource(5, items[14]), True))
    trades.append(Troc("Alchimiste de Sombre-Comté",TradeResource( 1, items[11]),TradeResource(8, items[17]), True))
    trades.append(Troc("Alchimiste de Sombre-Comté",TradeResource( 1, items[20]),TradeResource(12, items[15]), True))
    trades.append(Troc("Alchimiste de Sombre-Comté",TradeResource( 1, items[22]),TradeResource(5, items[7]), True))
    trades.append(Troc("Alchimiste de Sombre-Comté",TradeResource( 1, items[28]),TradeResource(4, items[23]), True))
    trades.append(Troc("Alchimiste de Sombre-Comté",TradeResource( 1, items[6]),TradeResource(5, items[16]), True))

    startGame = Game(hand, trades)
    gameManager = GameManager(startGame)
    print(gameManager)

    gameManager.incrementGeneration()
    print(gameManager)

    gameManager.incrementGeneration()
    print(gameManager)
