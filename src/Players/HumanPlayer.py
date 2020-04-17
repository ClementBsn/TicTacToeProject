from Player import Player

class HumanPlayer(Player):

    def __init__(self,name,pn):
        super().__init__(name,pn)

    def play(self,board):
        print("Select a line")
        x = input()
        print("Select a column")
        y = input()
        return int(x),int(y)
