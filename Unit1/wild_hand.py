


import itertools





all_ranks = '23456789TJQKA'
red_cards = [rank + suit for rank in all_ranks for suit in 'DH']
black_cards = [rank + suit for rank in all_ranks for suit in 'SC']



def best_wild_hand(hand):
    
    hands = set()


def replacements(card):
    
    if card == '?B':
        return black_cards
    elif card == '?R':
        return red_cards
    else:
      return [card]



def test():
    
    hand = "TD TC 5H 5C 7C ?R ?B".split()
    best_wild_hand(hand)



if '__main__' == __name__:
    test()
