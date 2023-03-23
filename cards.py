
def print_card(card):
    if card[0] == '10':
        print(" ___")
        print("|"+card[0] + " " + "|")
        print("| " + card[1] + " |")
        print("| " + card[0] + "|")
        print(" \u203e\u203e\u203e")

    else:
        print(" ___")
        print("|"+card[0] + "  " + "|")
        print("| " + card[1] + " |")
        print("|  " + card[0] + "|")
        print(" \u203e\u203e\u203e")


def print_hand(hand):
    values, suits = [], []
    for card in hand:
        values.append(card[0])
        suits.append(card[1])

    ret_str = " "
    ret_str += "___ " * len(hand)
    ret_str += "\n|"
    for value in values:
        if value == '10':
            ret_str += value + " |"
        else:
            ret_str += value + "  |"
    ret_str += "\n|"
    for suit in suits:
        ret_str += " " + suit + " |"
    ret_str += "\n|"
    for value in values:
        if value == '10':
            ret_str += " " + value + "|"
        else:
            ret_str += "  " + value + "|"
    ret_str += "\n "
    ret_str += "\u203e\u203e\u203e " * len(hand)
    ret_str += "\n  "
    for i in range(len(hand)):
        ret_str += str(i+1) + "   "

    return ret_str


def print_opponent(count):
    ret_str = " "
    ret_str += "___ " * count
    ret_str += "\n|"
    ret_str += "***|" * count
    ret_str += "\n|"
    ret_str += "*@*|" * count
    ret_str += "\n|"
    ret_str += "***|" * count
    ret_str += "\n "
    ret_str += "\u203e\u203e\u203e " * count
    return ret_str
