class Game:
    def __init__(self, startResources, startTrades):
        self.handResources = startResources;
        self.leftTrades = startTrades;

    def canDoTrade(trade):
        for i in range(len(self.handResources)):
            if self.handResources[i].name == trade.wantedResource.name:
                return self.handResources[i].quantity >= trade.wantedResource.quantity

        return false;

    def getDoablesTrades():
        doablesTrades = []
        for i in range(len(self.leftTrades)):
            if self.canDoTrade(self.leftTrades[i]):
                doablesTrades.append(self.leftTrades[i])

        return doablesTrades

    def clone():
        return Game(self.handResources, self.leftTrades)
