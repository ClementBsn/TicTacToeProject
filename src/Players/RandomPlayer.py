from Player import Player
import random

class RandomPlayer(Player):

    def __init__(self,name,pn):
        super().__init__(name,pn)

    def play(self,map):
        coordinates = []
        for i in range(3):
            for j in range(3):
                if map[i][j] == 0:
                    coordinates.append([i,j])

        return coordinates[int(random.random()*len(coordinates))]
