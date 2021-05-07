from classes.trades import TradeResource
from classes.trades import Troc
from classes.game import GameManager
from classes.game import Game
from classes.ThreadTest import ThreadTest

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
    trades.append(Troc("Forgeronne des Tarides",TradeResource( 1, items[23]),TradeResource(8, items[24]), True))
    trades.append(Troc("Forgeronne des Tarides",TradeResource( 1, items[8]),TradeResource(1, items[25]), True))
    trades.append(Troc("Forgeronne des Tarides",TradeResource( 1, items[22]),TradeResource(5, items[4]), True))
    trades.append(Troc("Forgeronne des Tarides",TradeResource( 1, items[26]),TradeResource(4, items[27]), True))
    trades.append(Troc("Forgeronne des Tarides",TradeResource( 1, items[28]),TradeResource(5, items[29]), True))
    

    #Alchimiste de Sombre-Comté
    trades.append(Troc("Alchimiste de Sombre-Comté",TradeResource( 1, items[29]),TradeResource(11, items[0]), True))
    trades.append(Troc("Alchimiste de Sombre-Comté",TradeResource( 1, items[5]),TradeResource(1, items[14]), True))
    trades.append(Troc("Alchimiste de Sombre-Comté",TradeResource( 1, items[11]),TradeResource(49, items[17]), True))
    trades.append(Troc("Alchimiste de Sombre-Comté",TradeResource( 1, items[20]),TradeResource(12, items[15]), True))
    trades.append(Troc("Alchimiste de Sombre-Comté",TradeResource( 1, items[22]),TradeResource(13, items[7]), True))
    trades.append(Troc("Alchimiste de Sombre-Comté",TradeResource( 1, items[28]),TradeResource(3, items[23]), True))
    trades.append(Troc("Alchimiste de Sombre-Comté",TradeResource( 1, items[6]),TradeResource(3, items[16]), True))
    

    #Marchand douteux
    trades.append(Troc("Marchand douteux",TradeResource( 1, items[23]),TradeResource(25, items[0]), True))
    trades.append(Troc("Marchand douteux",TradeResource( 1, items[24]),TradeResource(2, items[3]), True))
    trades.append(Troc("Marchand douteux",TradeResource( 1, items[29]),TradeResource(7, items[17]), True))
    trades.append(Troc("Marchand douteux",TradeResource( 1, items[25]),TradeResource(20, items[14]), True))
    trades.append(Troc("Marchand douteux",TradeResource( 1, items[11]),TradeResource(2, items[21]), True))
    trades.append(Troc("Marchand douteux",TradeResource( 1, items[19]),TradeResource(10, items[2]), True))
    trades.append(Troc("Marchand douteux",TradeResource( 1, items[21]),TradeResource(15, items[7]), True))
    

    #Maitre frabricant d'épées
    trades.append(Troc("Maitre frabricant d'épées",TradeResource( 1, items[14]),TradeResource(3, items[0]), True))
    trades.append(Troc("Maitre frabricant d'épées",TradeResource( 1, items[27]),TradeResource(4, items[3]), True))
    trades.append(Troc("Maitre frabricant d'épées",TradeResource( 1, items[21]),TradeResource(5, items[24]), True))
    trades.append(Troc("Maitre frabricant d'épées",TradeResource( 1, items[26]),TradeResource(1, items[6]), True))
    trades.append(Troc("Maitre frabricant d'épées",TradeResource( 1, items[25]),TradeResource(5, items[9]), True))
    trades.append(Troc("Maitre frabricant d'épées",TradeResource( 1, items[18]),TradeResource(3, items[29]), True))
    trades.append(Troc("Maitre frabricant d'épées",TradeResource( 1, items[8]),TradeResource(9, items[2]), True))
    

    #Enchantresse drakkari
    trades.append(Troc("Enchantresse drakkari",TradeResource( 1, items[7]),TradeResource(2, items[0]), True))
    trades.append(Troc("Enchantresse drakkari",TradeResource( 1, items[27]),TradeResource(5, items[7]), True))
    trades.append(Troc("Enchantresse drakkari",TradeResource( 1, items[13]),TradeResource(7, items[15]), True))
    trades.append(Troc("Enchantresse drakkari",TradeResource( 1, items[12]),TradeResource(9, items[14]), True))
    trades.append(Troc("Enchantresse drakkari",TradeResource( 1, items[11]),TradeResource(1, items[18]), True))
    trades.append(Troc("Enchantresse drakkari",TradeResource( 1, items[28]),TradeResource(4, items[20]), True))
    trades.append(Troc("Enchantresse drakkari",TradeResource( 1, items[6]),TradeResource(3, items[9]), True))
    

    #Mage de Dalaran
    trades.append(Troc("Mage de Dalaran",TradeResource( 10, items[0]),TradeResource(6, items[3]), False))
    trades.append(Troc("Mage de Dalaran",TradeResource( 18, items[0]),TradeResource(2, items[27]), False))
    trades.append(Troc("Mage de Dalaran",TradeResource( 60, items[0]),TradeResource(1, items[25]), False))
    trades.append(Troc("Mage de Dalaran",TradeResource( 138, items[0]),TradeResource(6, items[23]), False))
    trades.append(Troc("Mage de Dalaran",TradeResource( 205, items[0]),TradeResource(3, items[19]), False))
    

    #Forban de la Voile sanglante
    trades.append(Troc("Forban de la Voile sanglante",TradeResource( 18, items[0]),TradeResource(1, items[9]), False))
    trades.append(Troc("Forban de la Voile sanglante",TradeResource( 25, items[0]),TradeResource(10, items[7]), False))
    trades.append(Troc("Forban de la Voile sanglante",TradeResource( 120, items[0]),TradeResource(10, items[27]), False))
    trades.append(Troc("Forban de la Voile sanglante",TradeResource( 92, items[0]),TradeResource(4, items[18]), False))
    trades.append(Troc("Forban de la Voile sanglante",TradeResource( 240, items[0]),TradeResource(8, items[22]), False))
    

    #Apprenti pourpre
    trades.append(Troc("Apprenti pourpre",TradeResource( 13, items[0]),TradeResource(3, items[5]), False))
    trades.append(Troc("Apprenti pourpre",TradeResource( 14, items[0]),TradeResource(4, items[24]), False))
    trades.append(Troc("Apprenti pourpre",TradeResource( 30, items[0]),TradeResource(1, items[8]), False))
    trades.append(Troc("Apprenti pourpre",TradeResource( 150, items[0]),TradeResource(3, items[25]), False))
    trades.append(Troc("Apprenti pourpre",TradeResource( 166, items[0]),TradeResource(9, items[9]), False))
    

    #Champion de la main d'argent
    trades.append(Troc("Champion de la main d'argent",TradeResource( 11, items[0]),TradeResource(1, items[4]), False))
    trades.append(Troc("Champion de la main d'argent",TradeResource( 42, items[0]),TradeResource(6, items[29]), False))
    trades.append(Troc("Champion de la main d'argent",TradeResource( 72, items[0]),TradeResource(2, items[18]), False))
    trades.append(Troc("Champion de la main d'argent",TradeResource( 114, items[0]),TradeResource(2, items[28]), False))
    trades.append(Troc("Champion de la main d'argent",TradeResource( 125, items[0]),TradeResource(10, items[21]), False))
    

    #Aspirante de darnassus
    trades.append(Troc("Aspirante de darnassus",TradeResource( 6, items[0]),TradeResource(3, items[15]), False))
    trades.append(Troc("Aspirante de darnassus",TradeResource( 70, items[0]),TradeResource(1, items[11]), False))
    trades.append(Troc("Aspirante de darnassus",TradeResource( 50, items[0]),TradeResource(4, items[29]), False))
    trades.append(Troc("Aspirante de darnassus",TradeResource( 125, items[0]),TradeResource(5, items[6]), False))
    trades.append(Troc("Aspirante de darnassus",TradeResource( 166, items[0]),TradeResource(7, items[12]), False))
    

    #Parlevent
    trades.append(Troc("Parlevent",TradeResource( 15, items[0]),TradeResource(10, items[14]), False))
    trades.append(Troc("Parlevent",TradeResource( 25, items[0]),TradeResource(2, items[20]), False))
    trades.append(Troc("Parlevent",TradeResource( 65, items[0]),TradeResource(7, items[16]), False))
    trades.append(Troc("Parlevent",TradeResource( 70, items[0]),TradeResource(4, items[6]), False))
    trades.append(Troc("Parlevent",TradeResource( 180, items[0]),TradeResource(7, items[26]), False))
    

    #Défenseur d'Argus
    trades.append(Troc("Défenseur d'Argus",TradeResource( 10, items[0]),TradeResource(8, items[17]), False))
    trades.append(Troc("Défenseur d'Argus",TradeResource( 22, items[0]),TradeResource(3, items[13]), False))
    trades.append(Troc("Défenseur d'Argus",TradeResource( 70, items[0]),TradeResource(2, items[23]), False))
    trades.append(Troc("Défenseur d'Argus",TradeResource( 60, items[0]),TradeResource(7, items[20]), False))
    trades.append(Troc("Défenseur d'Argus",TradeResource( 204, items[0]),TradeResource(4, items[8]), False))



    startGame = Game(hand, trades)
    startGame.setIndex(0)
    gameManager = GameManager(startGame)
    gameManager.incrementGeneration()
    gameManagerThreads = []
    
    for game in gameManager.games:
        gameManagerThreads.append(ThreadTest(game, len(gameManagerThreads)))
    
    for thread in gameManagerThreads:
        thread.start()
    
