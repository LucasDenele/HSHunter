from threading import Thread 
from classes.game import GameManager

class ThreadTest(Thread):
    
    def __init__(self, game, index):
        Thread.__init__(self)
        self.game = game
        self.index = index
    
    def run(self):
        gameManager = GameManager(self.game)
        file = open("save"+str(self.index)+".txt","a")
        
        while(gameManager.isFinished() == False and gameManager.isCompleted() == False):
            gameManager.incrementGeneration()
            file.write("Thread n° : "+str(self.index)+" Génération : "+str(gameManager.generationNumber) +" Nb of games :"+str(len(gameManager.games))+"\n")
        
        print("Thread n° : ",self.index," est fini")
        file.write("Thread n° : "+str(self.index)+" est fini\n")
        
        print("Thread n° : ",self.index," completion :",gameManager.isCompleted())
        file.write("Thread n° : "+str(self.index)+" completion :"+str(gameManager.isCompleted())+"\n")

        gameManager = ""
        print(gameManager)

         