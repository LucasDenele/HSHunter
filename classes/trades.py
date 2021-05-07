class TradeResource:
    def __init__(self, object, quantity):
        # String with name of the resource
        self.object = object

        # Number of resources involved
        self.quantity = quantity

class Troc:
    def __init__(self, npcName, givenResource, wantedResource, isInfinite):
        # Name of the NPC
        self.npcName = npcName

        # The resource the user will receive
        self.givenResource = givenResource

        # The resource the user will lose
        self.wantedResource = wantedResource

        # Whether or not the user can do this trade infinitly
        self.infinite = isInfinite

        print(self.npcName, " ", self.givenResource.object, " ",self.givenResource.quantity, " ", self.wantedResource.object, " ",self.wantedResource.quantity, " ")
