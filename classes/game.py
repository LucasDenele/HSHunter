from .trades import TradeResource
import copy

class Game:
    def __init__(self, startResources, startTrades):
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

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        toPrint = "Current hand: \n"
        for i in range(len(self.handResources)):
            toPrint += self.handResources[i].__str__()

        toPrint += "Number of doables trades: " + str((len(self.getDoablesTrades()))) + "\n"
        return toPrint

class GameManager:
    def __init__(self, startGame):
        self.games = []
        self.games.append(startGame)
        self.generationNumber = 0

    def incrementGeneration(self):
        newGames = []
        for i in range(len(self.games)):
            currentGame = self.games[i]
            currentDoableTradeIndexes = currentGame.getDoablesTrades()
            for j in range(len(currentDoableTradeIndexes)):
                newGame = currentGame.clone()
                newGame.doTrade(currentDoableTradeIndexes[j])
                newGames.append(newGame)

        self.games = newGames
        self.generationNumber += 1

    def __str__(self):
        toPrint = "Generation n°" + str(self.generationNumber) + "\n"
        toPrint += "Number of games: " + str(len(self.games)) + "\n"
        for i in range(len(self.games)):
            toPrint += self.games[i].__str__()
        return toPrint
