from utils import *

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

    def restart(self):
        self.map = [[0,0,0],[0,0,0],[0,0,0]]
        self.is_playing = 0
        self.winner = 0
        self.nb_turn = 1

    def end_turn(self):
        self.is_playing *= -1
        self.nb_turn += 1

    def declare_winner(self,winner):
        self.winner = winner

    def get_winner(self):
        return self.winner
