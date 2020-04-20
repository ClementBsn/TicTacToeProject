from Players.NNPlayer import NNPlayer
from Players.RandomPlayer import RandomPlayer

from play import *

import numpy as np
import random
import math

def PDE(nb_gen,dimension,min_dim,max_dim):
    player = NNPlayer("James",1,[],1,False)
    size_pop = int(10+math.sqrt(dimension))
    f = 0.75
    f_ = 1 - f
    p_m = 0.025
    c_r = 0.8

    population = dict()
    fitness = dict()
    best = 0
    fit_best = -1 * float('inf')

    for k in range(size_pop):
        invidual = np.random.uniform(min_dim,max_dim,dimension)
        fit = calculate_fitness(invidual,player)
        if fit > fit_best:
            best = invidual
            fit_best = fit
        population[k] = invidual
        fitness[k] = fit

    for g in range(nb_gen):
        for index in range(size_pop):
            while True:
                a = int(random.random() * size_pop)
                if a != index:
                    break
            while True:
                b = int(random.random() * size_pop)
                if b != index and b != a:
                    break
            while True:
                c = int(random.random() * size_pop)
                if c != index and c != a and c != b:
                    break

            mutant = population[a] + f * (population[b] - population[c]) + f_ * (best - population[a])

            if random.random() < p_m:
                while True:
                    d = int(random.random() * size_pop)
                    if d != index and d != a and d != b and d != c:
                        break
                mutant = mutant + np.random.uniform(-1,1,dimension) + population[d]

            m = random.random() * dimension
            child = np.zeros((1,dimension))[0]
            for j in range(dimension):
                if random.random() < c_r or j == m:
                    if mutant[j] > max_dim:
                        mutant[j] = max_dim
                    if mutant[j] < min_dim:
                        mutant[j] = min_dim
                    child[j] = mutant[j]
                else:
                    child[j] = population[index][0]

            fit = calculate_fitness(child,player)

            if fit > fitness[index]:
                fitness[index] = fit
                population[index] = child

                if fit > fit_best:
                    best = child
                    fit_best = fit
        if g % 100 == 0:
            print("###### "+str(g)+" ######")
            print(fit_best)
    player.set_vector(best)
    player.save()


def calculate_fitness(invidual,player):
    player.set_vector(invidual)
    p2 = RandomPlayer("John",-1)
    B = Board(player,p2)
    score = play_100_games(B)
    return score["P1"]

PDE(1000,351,-20,20)
