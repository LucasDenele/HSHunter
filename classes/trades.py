class TradeResource:
    def __init__(self, quantity, name):
        # String with name of the resource
        self.name = name

        # Number of resources involved
        self.quantity = quantity

    def __str__(self):
        return "[" + str(self.quantity) + " x " + str(self.name) + "]"

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
    
    def __str__(self):
        return "{ " + str(self.npcName) + " : " + str(self.givenResource) + " = " + str(self.wantedResource) + " }"
