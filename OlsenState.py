import random
from cards import Deck
from meta import GameMeta


class OlsenState:
    def __init__(self) -> None:
        self.to_play = GameMeta.PLAYERS['one']
        self.deck = [(v, s) for v in ['A', '2', '3', '4', '5', '6', '7',
                                      '8', '9', '10', 'J', 'Q', 'K'] for s in ['H', 'D', 'C', 'S']]
        random.shuffle(self.deck)
        self.human_hand = [self.draw() for _ in range(5)]
        self.table = [self.draw()]

        self.agent_hand = [self.draw() for _ in range(5)]

    def game_over(self) -> bool:
        if len(self.human_hand) == 0 or len(self.agent_hand) == 0:
            return True
        else:
            return False

    def get_outcome(self):
        if len(self.human_hand) == 0:
            return GameMeta.OUTCOMES['one']
        else:
            return GameMeta.OUTCOMES['two']

    def is_legal(self, card) -> bool:
        if card[0] == '8':
            return True
        if card[0] == self.table[-1][0] or card[1] == self.table[-1][1]:
            return True
        return False

    def get_legal_moves(self) -> list:

        legals = []
        if self.to_play == GameMeta.PLAYERS['one']:
            for card in self.human_hand:
                if self.is_legal(card):
                    legals.append(card)
            if len(legals) == 0:
                for _ in range(3):
                    drawn_card = self.human_draw()
                    if self.is_legal(drawn_card):
                        legals.append(card)
                        break

        else:
            for card in self.agent_hand:
                if self.is_legal(card):
                    legals.append(card)
            if len(legals) == 0:
                for _ in range(3):
                    drawn_card = self.agent_draw()
                    if self.is_legal(drawn_card):
                        legals.append(card)
                        break

        return legals

    def draw(self) -> tuple:
        card = self.deck.pop()
        return card

    def human_draw(self) -> tuple:
        card = self.draw()
        self.human_hand.append(card)
        return card

    def agent_draw(self) -> tuple:
        card = self.draw()
        self.agent_hand.append(card)
        return card

    def move(self, card) -> None:
        if card != None:
            self.table.append(card)
            if self.to_play == GameMeta.PLAYERS['one']:
                self.human_hand.remove(card)
            else:
                self.agent_hand.remove(card)
        if self.to_play == GameMeta.PLAYERS['one']:
            self.to_play = GameMeta.PLAYERS['two']
        else:
            self.to_play = GameMeta.PLAYERS['one']

    def print(self) -> None:
        print("Table:")
        print(self.table[-1])
        print("human hand:")
        for i in range(len(self.human_hand)):
            print(str(i)+"." +
                  str(self.human_hand[i][0])+str(self.human_hand[i][1]))
