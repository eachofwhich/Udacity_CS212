# -----------------
# User Instructions
# 
# Write a strategy function, clueless, that ignores the state and
# chooses at random from the possible moves (it should either 
# return 'roll' or 'hold'). Take a look at the random library for 
# helpful functions.

import random

possible_moves = ['roll', 'hold']

def clueless(state):
    "A strategy that ignores the state and chooses at random from possible moves."
    return random.choice(possible_moves)


def test():
	
	assert clueless(None) in possible_moves

	print('all good.')





if __name__ == '__main__':
	test()