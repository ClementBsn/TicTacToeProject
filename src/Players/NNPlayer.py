from Player import Player
from Players.NN.NN_Architecture import NN_Architecture

from utils import *
import copy
import random

class NNPlayer(Player):

    def __init__(self,name,pn,vector_wb,nn_architecture,loading=True):
        self.NN = NN_Architecture("bla.json",nn_architecture)
        if loading:
            self.load()
        """else:
            self.initialize(vector_wb)"""
        super().__init__(name,pn)

    def play(self,board):
        new_map = self.translate_map(board.map)
        moves = self.NN.process(new_map)
        poss_moves = get_allowed_moves(board.map)
        for move in moves.keys():
            if not(list(number_to_coordinates(move)) in poss_moves):
                moves[move] = -1 * float('inf')
        max_val = max(moves.values())
        cpt = list(moves.values()).count(max_val)
        if cpt > 1:
            best_moves = [number_to_coordinates(x) for x in moves.keys() if moves[x] == max_val]
            move = best_moves[int(random.random()*len(best_moves))]
        else:
            move = [number_to_coordinates(x) for x in moves.keys() if moves[x] == max_val][0]
        return move

    def translate_map(self,map):
        new_map = copy.deepcopy(map)
        if self.player_number != 1:
            for i in range(3):
                for j in range(3):
                    if new_map[i][j] == 1:
                        new_map[i][j] == -1
                    if new_map[i][j] == -1:
                        new_map[i][j] == 1
        return new_map

    def save(self):
        self.NN.save()

    def load(self):
        self.NN.load()

    def set_vector(self,vector):
        self.NN.initialize(vector)
