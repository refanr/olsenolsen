import random
from cards import print_card, print_hand, print_opponent
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
        if len(legals) == 0:
            legals.append(('x', 'x'))
        return legals

    def draw(self) -> tuple:
        if len(self.deck) != 0:
            card = self.deck.pop()
            return card
        else:
            self.reshuffle()
            return self.draw()

    def reshuffle(self) -> None:
        self.deck.extend(self.table)
        self.table.clear()
        card = self.draw()
        self.table.append(card)

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
            if card == ('x', 'x'):
                pass
            else:
                self.table.append(card)
                if self.to_play == GameMeta.PLAYERS['one']:
                    try:
                        self.human_hand.remove(card)
                    except:
                        pass
                elif self.to_play == GameMeta.PLAYERS['two']:
                    try:
                        self.agent_hand.remove(card)
                    except:
                        pass
        if self.to_play == GameMeta.PLAYERS['one']:
            self.to_play = GameMeta.PLAYERS['two']
        else:
            self.to_play = GameMeta.PLAYERS['one']

    def print(self) -> None:
        print("Agent hand:")
        print(print_opponent(len(self.agent_hand)))
        print("Table:")
        print_card(self.table[-1])
        print("Human hand:")
        print(print_hand(self.human_hand))
        # for i in range(len(self.human_hand)):
        #     print(str(i+1)+":")
        #     print_card(self.human_hand[i])
