from Player import Player
from Board import Board
from Players.HumanPlayer import HumanPlayer
from Players.RandomPlayer import RandomPlayer
from Players.MinMaxPlayer import MinMaxPlayer

from utils import *

import random

def play_a_move(board):
    x,y = (-1,-1)
    if board.is_playing == 1:
        while(True):
            x,y = board.player1.play(board)
            if board.map[x][y] == 0:
                board.map[x][y] = board.is_playing
                return x,y

    if board.is_playing == -1:
        while(True):
            x,y = board.player2.play(board)
            if board.map[x][y] == 0:
                board.map[x][y] = board.is_playing
                return x,y

def play_a_game(board):
    board.display_map()

    if board.is_playing == 0:
        if random.random() < 0.5:
            board.is_playing = 1
        else:
            board.is_playing = -1

    for i in range(9):
        if board.is_playing == 1:
            print("Player 1 is playing...")
        else:
            print("Player 2 is playing...")

        x,y = play_a_move(board)
        b, winner = get_winner(board.map)
        if b:
            board.display_map()
            if winner == 1:
                print("Player 1 won !")
            else:
                print("Player 2 won !")
            break

        if board.is_playing == 1:
            board.is_playing = -1
        else:
            board.is_playing = 1

        board.nb_turn += 1
        board.display_map()

def play_100_games(board):
    scores = {"P1":0, "P2":0,"Nul":0}

    for i in range(100):
        if board.is_playing == 0:
            if random.random() < 0.5:
                board.is_playing = 1
            else:
                board.is_playing = -1

        for i in range(9):
            if len(get_allowed_moves(board.map)) == 0:
                break
            x,y = play_a_move(board)
            b, winner = get_winner(board.map)
            if b:
                board.declare_winner(winner)
                break

            board.end_turn()

        if board.get_winner() == 1:
            scores["P1"] += 1
        else:
            if board.get_winner() == -1:
                scores["P2"] += 1
            else:
                scores["Nul"] += 1

        board.restart()

    print(scores)

p1 = MinMaxPlayer("Jack",1,6)
p2 = MinMaxPlayer("John",1,1)
B = Board(p1,p2)
#play_a_game(B)
play_100_games(B)
