from Player import Player
from utils import *

import numpy as np
import copy
import random

class AlphaBetaPlayer(Player):

    def __init__(self,name,player_number,deepness_max):
        self.deepness_max = deepness_max
        super().__init__(name,player_number)

    def play(self,board):
        return self.search_a_move_AB(board.map,board.nb_turn)[0]

    def search_a_move_AB(self,map,turn,alpha=-1*float('inf'),beta=float('inf'),deep=1):
        poss_moves = get_allowed_moves(map)
        evaluation_moves = dict()
        a = alpha
        b = beta

        if deep % 2 == 0:
            player = self.player_number * -1
        else:
            player = self.player_number

        if deep % 2 == 0:
            v = float('inf')
            for move in poss_moves:
                new_map = self.simulate_move(map,move,player)
                value, is_winning_move = self.evaluate_move(new_map,move,player)
                if not(is_winning_move or deep == self.deepness_max or turn == 9):
                    value += self.search_a_move_AB(new_map,turn+1,a,b,deep+1)[1]
                evaluation_moves[coordinates_to_number(move[0],move[1])] = value
                v = min(v,value)
                if a >= v:
                    return move, value
                b = min(b,v)

            min_val = min(evaluation_moves.values())
            cpt = list(evaluation_moves.values()).count(min_val)
            if cpt > 1:
                poss_moves = [number_to_coordinates(x) for x in evaluation_moves.keys() if evaluation_moves[x] == min_val]
                move = poss_moves[int(random.random()*len(poss_moves))]
            else:
                move = [number_to_coordinates(x) for x in evaluation_moves.keys() if evaluation_moves[x] == min_val][0]

            return move, min_val

        else:
            v = -1 * float('inf')
            for move in poss_moves:
                new_map = self.simulate_move(map,move,player)
                value, is_winning_move = self.evaluate_move(new_map,move,player)
                if not(is_winning_move or deep == self.deepness_max or turn == 9):
                    value += self.search_a_move_AB(new_map,turn+1,a,b,deep+1)[1]

                evaluation_moves[coordinates_to_number(move[0],move[1])] = value
                v = max(v,value)
                if v >= b:
                    return move, value
                a = max(a,v)

            max_val = max(evaluation_moves.values())
            cpt = list(evaluation_moves.values()).count(max_val)
            if cpt > 1:
                poss_moves = [number_to_coordinates(x) for x in evaluation_moves.keys() if evaluation_moves[x] == max_val]
                move = poss_moves[int(random.random()*len(poss_moves))]
            else:
                move = [number_to_coordinates(x) for x in evaluation_moves.keys() if evaluation_moves[x] == max_val][0]

            return move, max_val

    def simulate_move(self,map,move,player):
        new_map = copy.deepcopy(map)
        new_map[move[0]][move[1]] = player
        return new_map

    def evaluate_move(self,map,last_move,player):
        value = 0
        is_winning_move = False

        if player == self.player_number:
            c1 = 1
            c2 = -1
        else:
            c1 = -1
            c2 = 1

        b,winner = get_winner(map)
        if b and winner == self.player_number:
            value += 100
            is_winning_move = True
        if b and winner != self.player_number:
            value += -100
            is_winning_move = True

        l_c_d = get_line(map,last_move[0])
        value += l_c_d.count(player) * 10 * c1
        value += l_c_d.count(int(player*-1)) * 10 * c2

        l_c_d = get_column(map,last_move[1])
        value += l_c_d.count(player) * 10 * c1
        value += l_c_d.count(int(player*-1)) * 10 * c2

        l_c_d = get_first_diag(map)
        if last_move in l_c_d:
            value -= 10
            value += l_c_d.count(player) * 10 * c1
            value += l_c_d.count(int(player*-1)) * 10 * c2

        l_c_d = get_second_diag(map)
        if last_move in l_c_d:
            value -= 10
            value += l_c_d.count(player) * 10 * c1
            value += l_c_d.count(int(player*-1)) * 10 * c2

        return value, is_winning_move
