import random


def deal(hand1, hand2, deck):
    for i in range(5):
        card = random.choice(deck)
        hand1.append(card)
        deck.remove(card)
        card = random.choice(deck)
        hand2.append(card)
        deck.remove(card)


def draw_from_deck(hand, deck):
    card = random.choice(deck)
    hand.append(card)
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


def no_legal_moves(hand, deck, table):
    for i in range(3):
        draw_from_deck(hand, deck)
        if is_legal(hand[-1], table):
            play_card(hand[-1], table)


def re_shuffle(deck, table):
    deck.extend(table)
    table.clear()
    draw_from_deck(table, deck)


def random_move(hand, deck, table):
    for card in hand:
        if is_legal(card, table):
            play_card(card, table)
            hand.remove(card)
            return True
    no_legal_moves(hand, deck, table)


def make_deck():
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = ['H', 'D', 'C', 'S']
    deck = [(v, s) for v in values for s in suits]
    return deck


def print_card(card):
    ret_str = ''
    if card[1] == 'H':
        ret_str += '♥'
    elif card[1] == 'D':
        ret_str += '♦'
    elif card[1] == 'C':
        ret_str += '♣'
    elif card[1] == 'S':
        ret_str += '♠'
    ret_str += card[0]
    return ret_str


def play():
    deck = make_deck()

    player = []
    rando = []

    table = []

    draw_from_deck(table, deck)
    deal(player, rando, deck)

    player_turn = True
    game_over = False

    while (game_over == False):
        if player_turn:

            print('Player hand: ', player)
            print('Table: ' + print_card(table[-1]))
            print('Enter card to play: ')
            card = input()
            if card == 'D':
                no_legal_moves(player, deck, table)
                player_turn = False
                continue
            card = card.split()
            card = (card[0], card[1])
            if play_card(card, table):
                player.remove(card)
                player_turn = False
            else:
                print('Illegal move')
        else:
            print('Rando turn')
            random_move(rando, deck, table)
            print('Table: ', print_card(table[-1]))
            player_turn=True

        if (len(player) == 0):
            print('Player wins')
            game_over=True
        elif (len(rando) == 0):
            print('Rando wins')
            game_over=True


if __name__ == '__main__':
    play()
