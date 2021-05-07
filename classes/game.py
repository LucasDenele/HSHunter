from .trades import TradeResource
import copy

class Game:
    def __init__(self, startResources, startTrades):
        self.index = -1
        self.handResources = startResources
        self.leftTrades = startTrades
        self.tradeHistory = []

    def changeHandResource(self, index, quantity):
        self.handResources[index].quantity += quantity

    def canDoTrade(self, indexes):
        if self.handResources[indexes[1]].name == self.leftTrades[indexes[0]].wantedResource.name :
            return self.handResources[indexes[1]].quantity >= self.leftTrades[indexes[0]].wantedResource.quantity

        return False;

    def getDoablesTrades(self):
        doableTradeIndexes = []
        for i in range(len(self.leftTrades)):
            for j in range(len(self.handResources)):
                if self.canDoTrade((i, j)):
                    doableTradeIndexes.append((i, j))

        return doableTradeIndexes

    def doTrade(self, indexes):
        if (self.leftTrades[indexes[0]].infinite):
            quantityOfNewItem = 0
            while (self.canDoTrade(indexes)):
                quantityOfNewItem += self.leftTrades[indexes[0]].givenResource.quantity
                self.changeHandResource(indexes[1], - self.leftTrades[indexes[0]].wantedResource.quantity)
            self.handResources.append(TradeResource(quantityOfNewItem, self.leftTrades[indexes[0]].givenResource.name))
        else:
            self.changeHandResource(indexes[1], - self.leftTrades[indexes[0]].wantedResource.quantity)
            self.handResources.append(TradeResource(self.leftTrades[indexes[0]].givenResource.quantity, self.leftTrades[indexes[0]].givenResource.name))
            self.leftTrades.remove(self.leftTrades[indexes[0]])
        for tradeResource in self.handResources:
            if(tradeResource.quantity == 0):
                self.handResources.remove(tradeResource)

    def clone(self):
        return copy.deepcopy(self)
    
    def setIndex(self, index):
        self.index = index

    def __str__(self):
        toPrint = "Game Index : " + str(self.index) + "\n"
        toPrint += "Current hand: \n"
        for i in range(len(self.handResources)):
            toPrint += self.handResources[i].__str__()

        toPrint += "Number of doables trades: " + str((len(self.getDoablesTrades()))) + "\n"
        return toPrint

class GameManager:
    def __init__(self, startGame):
        self.games = []
        self.lastGameIndex = 0
        self.games.append(startGame)
        self.generationNumber = 0

    def incrementGeneration(self):
        newGames = []
        for i in range(len(self.games)):
            currentGame = self.games[i]
            currentDoableTradeIndexes = currentGame.getDoablesTrades()
            for j in range(len(currentDoableTradeIndexes)):
                newGame = currentGame.clone()
                self.lastGameIndex += 1
                newGame.setIndex(self.lastGameIndex)
                newGame.doTrade(currentDoableTradeIndexes[j])
                newGames.append(newGame)

        self.games = newGames
        self.generationNumber += 1
    
    def isFinished(self):
        for game in self.games:
            if((len(game.getDoablesTrades())) != 0):
                return False
        return True
    
    def isCompleted(self):
        for game in self.games:
            for trader in game.leftTrades:
                    if(not trader.infinite):
                        return False
        return True

    def __str__(self):
        return "Generation n°" + str(self.generationNumber) + "\n" + "Number of games: " + str(len(self.games)) + "\n"

