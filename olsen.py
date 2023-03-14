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
        if len(deck) != 0:
            draw_from_deck(hand, deck)
        else:
            re_shuffle(deck, table)
        if is_legal(hand[-1], table):
            play_card(hand[-1], table)


def re_shuffle(deck, table):
    deck.extend(table)
    table.clear()
    draw_from_deck(table, deck)


def check_for_doubles(card, hand):
    for c in hand:
        if c[0] == card[0] or c[1] == card[1]:
            return True
    return False


def get_doubles(card, hand):
    for c in hand:
        if c[0] == card[0] or c[1] == card[1]:
            return c


def random_move(hand, deck, table):
    for card in hand:
        if is_legal(card, table):
            play_card(card, table)
            hand.remove(card)
            if (check_for_doubles(table[-1], hand)):
                card2 = get_doubles(table[-1], hand)
                play_card(card2, table)
                hand.remove(card2)
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


def initialize():
    deck = make_deck()

    player = []
    rando = []

    table = []

    draw_from_deck(table, deck)
    deal(player, rando, deck)

    return (deck, player, rando, table)


def play(player_score=0, rando_score=0):
    (deck, player, rando, table) = initialize()

    player_turn = True
    game_over = False

    while (game_over == False):
        if player_turn:
            #print('Player turn')
            random_move(player, deck, table)
            #print('Table: ', print_card(table[-1]))
            player_turn = False

            # print('Player hand: ', player)
            # print('Table: ' + print_card(table[-1]))
            # print('Enter card to play: ')
            # card = input()
            # if card == 'D':
            #     no_legal_moves(player, deck, table)
            #     player_turn = False
            #     continue
            # card = card.split()
            # card = (card[0], card[1])
            # if play_card(card, table):
            #     player.remove(card)
            #     player_turn = False
            # else:
            #     print('Illegal move')
        else:
            #print('Rando turn')
            random_move(rando, deck, table)
            #print('Table: ', print_card(table[-1]))
            player_turn = True

        if (len(player) == 0):
            #print('Player wins')
            player_score += 1
            game_over = True
        elif (len(rando) == 0):
            #print('Rando wins')
            rando_score += 1
            game_over = True
    return (player_score, rando_score)


if __name__ == '__main__':
    play()
