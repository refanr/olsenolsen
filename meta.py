import math


class GameMeta:
    PLAYERS = {'none': 0, 'one': 1, 'two': 2}
    OUTCOMES = {'none': 0, 'one': 1, 'two': 2}
    INF = float('inf')


class MCTSMeta:
    EXPLORATION = math.sqrt(2)
