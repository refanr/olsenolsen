import math
import olsen
from meta import GameMeta, MCTSMeta


class Node:
    def __init__(self, move, parent) -> None:
        self.move = move
        self.parent = parent
        self.N = 0
        self.Q = 0
        self.children = {}
        self.outcome = GameMeta.PLAYERS['none']
        
    def add_children(self, children) -> None:
        for child in children:
            self.children[child.move] = child

    def value(self, explore = MCTSMeta.EXPLORATION):
        if self.N == 0:
            return 0 if explore == 0 else GameMeta.INF
        else:
            return self.Q / self.N + explore * math.sqrt(math.log(self.parent.N) / self.N)


class MCTS:
    def __init__(self) -> None:
        pass
