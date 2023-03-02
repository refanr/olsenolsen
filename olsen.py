import random

def deal(hand1, hand2, deck):
    for i in range(5):
        card = random.choice(deck)
        hand1.append(card)
        deck.remove(card)
        card = random.choice(deck)
        hand2.append(card)
        deck.remove(card)

def draw(hand, deck):
    card = random.choice(deck)
    hand.append(card)
    deck.remove(card)
    
def init_game(table, deck):
    
    card = random.choice(deck)
    table.append(card)
    deck.remove(card)

def is_legal(card, table):
    if card[0] == 8:
        return True
    if card[0] == table[-1][0] or card[1] == table[-1][1]:
        return True
    else:
        return False

def play_card(card, table):
    if is_legal(card, table):
        table.append(card)
        return True
    else:
        print('Illegal move')
        
def no_legal_moves(hand, deck):
    for i in range(3):
        draw(hand, deck)
        if is_legal(hand[-1], table):
            play_card(hand[-1], table)
        
  
        
    
    
    
    

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
deck = [(v, s) for v in values for s in suits]

hand1 = []
hand2 = []

table = []

init_game(table, deck)
deal(hand1, hand2, deck)
    
print(table[-1])
print(hand1)
print(hand2)
print(len(deck))



