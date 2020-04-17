from Player import Player

class HumanPlayer(Player):

    def __init__(self,name,pn):
        super().__init__(name,pn)

    def play(self,map):
        print("Select a line")
        x = input()
        print("Select a column")
        y = input()
        return int(x),int(y)
