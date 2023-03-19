import random


class Deck:
    def __init__(self) -> None:
        self.deck = [(v, s) for v in ['A', '2', '3', '4', '5', '6', '7',
                                      '8', '9', '10', 'J', 'Q', 'K'] for s in ['H', 'D', 'C', 'S']]
        random.shuffle(self.deck)
        
    
