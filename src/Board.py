from Player import Player

from Players.HumanPlayer import HumanPlayer
from Players.RandomPlayer import RandomPlayer

import random

class Board:

    def __init__(self,p1,p2):
        self.map = [[0,0,0],[0,0,0],[0,0,0]]
        self.is_playing = 0
        self.winner = 0
        self.nb_turn = 1
        self.player1 = p1
        self.player2 = p2

    def display_map(self):
        d_map = "Turn : "+str(self.nb_turn)+"\n\n+-----+\n"
        for i in range(3):
            for j in range(3):
                d_map += "|"
                if self.map[i][j] == 0:
                    d_map += " "
                if self.map[i][j] == 1:
                    d_map += "o"
                if self.map[i][j] == -1:
                    d_map += "*"
            d_map += "|\n+-----+\n"

        print(d_map)

    def play_a_move(self):
        x,y = (-1,-1)
        if self.is_playing == 1:
            while(True):
                x,y = self.player1.play(self.map)
                if self.map[x][y] == 0:
                    self.map[x][y] = self.is_playing
                    return x,y

        if self.is_playing == -1:
            while(True):
                x,y = self.player2.play(self.map)
                if self.map[x][y] == 0:
                    self.map[x][y] = self.is_playing
                    return x,y

    def is_winning(self,x,y):
        if self.map[x][0] == self.map[x][1] and self.map[x][0] == self.map[x][2]:
            return True
        if self.map[0][y] == self.map[1][y] and self.map[0][y] == self.map[2][y]:
            return True
        diag1 = [[0,0],[1,1],[2,2]]
        diag2 = [[0,2],[1,1],[2,0]]
        if [x,y] in diag1:
            if self.map[0][0] == self.map[1][1] and self.map[0][0] == self.map[2][2]:
                return True
        if [x,y] in diag2:
            if self.map[0][2] == self.map[1][1] and self.map[0][2] == self.map[2][0]:
                return True
        return False

    def play_a_game(self):
        self.display_map()

        if self.is_playing == 0:
            if random.random() < 0.5:
                self.is_playing = 1
            else:
                self.is_playing = -1

        while True:
            if self.is_playing == 1:
                print("Player 1 is playing...")
            else:
                print("Player 2 is playing...")

            x,y = self.play_a_move()
            b = self.is_winning(x,y)
            if b:
                self.display_map()
                if self.is_playing == 1:
                    print("Player 1 won !")
                else:
                    print("Player 2 won !")
                break

            if self.is_playing == 1:
                self.is_playing = -1
            else:
                self.is_playing = 1

            self.nb_turn += 1
            self.display_map()



p1 = HumanPlayer("Jack")
p2 = RandomPlayer("Joe")
B = Board(p1,p2)
print(B.play_a_game())
