# https://www.codewars.com/kata/5a360620f28b82a711000047/train/python

# Define a card suit

def define_suit(card):
    if card[-1] == "C":
        return 'clubs'
    elif card[-1] == "S":
        return 'spades'
    elif card[-1] == "D":
        return 'diamonds'
    elif card[-1] == "H":
        return 'hearts'
