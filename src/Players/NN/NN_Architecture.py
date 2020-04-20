import numpy as np
import json

class NN_Architecture():

    def __init__(self,path_to_save,nb_arch):
        self.path_to_save = path_to_save
        self.nb_arch = nb_arch
        self.layers = dict()

    def process(self,map):
        if self.nb_arch == 1:
            values = self.process_arch_1(map)[0]
            moves = dict()
            for i in range(len(values)):
                moves[i] = values[i]
            return moves

    def initialize(self,vector):
        if self.nb_arch == 1:
            self.init_arch_1(vector)

    def init_arch_1(self,vector):
        self.layers["W0"] = np.reshape(vector[:9*18],(9,18))
        self.layers["B0"] = np.reshape(vector[9*18:9*18+18],(1,18))
        self.layers["W1"] = np.reshape(vector[9*18+18:9*18+18+18*9],(18,9))
        self.layers["B1"] = np.reshape(vector[9*18+18+18*9:],(1,9))

    def process_arch_1(self,map):
        input = np.reshape(map,(1,9))
        value = self.sigmoid(np.matmul(input,self.layers["W0"]) + self.layers["B0"])
        return self.sigmoid(np.matmul(value,self.layers["W1"]) + self.layers["B1"])

    def sigmoid(self,value):
        return 1 / (1 + np.exp(-value))

    def save(self):
        with open(self.path_to_save,'w') as outfile:
            json.dump(self.layers,outfile)

    def load(self):
        with open(self.path_to_save,'r') as outfile:
            self.layers = json.load(outfile)
