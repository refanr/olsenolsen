from cards import Card, Deck
from meta import GameMeta


class OlsenState:
    def __init__(self) -> None:
        self.to_play = GameMeta.PLAYERS['one']
        self.human_hand = [self.draw() * 5]
        self.table = [self.draw()]
        self.deck = Deck()
        self.agent_hand = [self.draw() * 5]

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

    def get_legal_moves(self) -> list:

        legals = []
        for card in self.human_hand:
            if card[0] == '8':
                legals.append(card)
            if card[0] == self.table[-1][0] or card[1] == self.table[-1][1]:
                legals.append(card)
        for card in self.agent_hand:
            if card[0] == '8':
                legals.append(card)
            if card[0] == self.table[-1][0] or card[1] == self.table[-1][1]:
                legals.append(card)

        return legals

    def draw(self) -> tuple:
        return self.deck.deck.pop()

    def human_draw(self) -> tuple:
        card = self.draw()
        self.human_hand.append()
        return card

    def agent_draw(self) -> tuple:
        card = self.draw()
        self.human_agent.append()
        return card

    def move(self, card) -> None:
        self.table.append(card)
        if self.to_play == GameMeta.PLAYERS['one']:
            self.human_hand.remove(card)
        else:
            self.agent_hand.remove(card)
        self.to_play = GameMeta.PLAYERS['two'] if self.to_play == GameMeta.PLAYERS['one'] else GameMeta.PLAYERS['one']

    def print(self) -> None:
        print("Table:")
        print(self.table[-1])
        print("human hand:")
        for i in range(len(self.human_hand)):
            print(str(i)+"." +
                  str(self.human_hand[i][0])+str(self.human_hand[i][1]))
