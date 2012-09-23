
million = 10**6



def best_action(state, actions, Q, U):
	def EU(action): return Q(state, action, U)
	print map(EU, actions(state))
	return max(actions(state), key = EU)



def actions(state): return ['hold', 'gamble']

def identity(x): return x

U = identity



def Q(state, action, U):
	"""Return the expected value of action in state, according to utility U."""
	if 'hold' == action:
		return U(state + 1 * million)

	if action == 'gamble':
		return U(state + 3 * million) * 0.5 + U(state) * 0.5


import math
print best_action(100, actions, Q, U)
print best_action(million, actions, Q, math.log10)