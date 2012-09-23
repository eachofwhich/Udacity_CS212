# Game of Pig implementation from unit 5.

import random
from functools import update_wrapper





def decorator(fn):
	
	def decorate(arg_fn):
		return update_wrapper(fn(arg_fn), arg_fn)
	update_wrapper(decorate, fn)
	return decorate



@decorator
def memo(fn):
	"""Memoize decorator."""
	cache = {}

	def decorate(*args):
		try:
			return cache[args]
		except KeyError:
			cache[args] = result = fn(*args)
			return result
		except TypeError:
			return fn(*args)

	return decorate



class Pig:

	def __init__(self, goal = 50):
		self.__actions = ['roll', 'hold']
		self.__goal = goal



	def get_actions(self): return self.__actions

	def next_actions(self, state): return self.get_actions() if state[3] else ['roll']

	def roll_die(self):
		while True: yield random.randint(1, 6)



	def __other_turn(self, turn):
		return 0 if turn else 1



	def hold(self, state):
		"""This performs the hold action for the current player, and returns the next state."""
		turn, player1, player2, pending = state
		return (self.__other_turn(turn), player2, player1 + pending, 0)



	def roll(self, state, die):
		"""This performs the roll action for the current player, and returns the next state."""
		turn, player1, player2, pending = state

		if die is 1:
			return (self.__other_turn(turn), player2, player1 + die, 0)
		else:
			return (turn, player1, player2, pending + die)



	def strategy_clueless(self, state):
		""""This is an actual strategy function that returns an random action."""
		return random.choice(self.__actions)



	def hold_at_factory(self, at):
		"""This is a strategy function factory that returns a strategy function to automatically hold at `at`."""
		
		def fn(state):
			
			turn, player1, player2, pending = state
			if pending >= at or pending + player1 >= self.__goal:
				return 'hold'
			else:
				return 'roll'

		return fn



	@memo
	def Q(self, state, action, U):
		"""Return the value of action in state, according to unility U."""
		if 'hold' == action:
			return 1 - U(self.hold(state))

		if 'roll' == action:
			return (
					1 - U( self.roll(state, 1)) + sum( U(self.roll(state, die)) for die in (2, 3, 4, 5, 6) )
				) / 6

		raise ValueError('Illegal action {}'.format(action))



	def U(self, state):
		"""Return the unility of state by backtracking from end states."""
		turn, player_a, player_b, pending = state

		# Base case for win state.
		if player_a + pending >= self.__goal: return 1

		# Base case for lose state.
		if player_b >= self.__goal: return 0

		# Recursively calculate the quality of each next action, and return the max.

		return max( self.Q(state, action, self.U) for action in self.next_actions(state) )



	def best_action(self, state, actions, Q, U):
		"""Return the next action with highest quality."""
		def trace_quality(action): return Q(state, action, U)
		return max(actions(state), key=trace_quality)



	def max_wins(self, state):
		"""Return action with highest quality."""
		return self.best_action(state, self.next_actions, self.Q, self.U)



	def play(self, player_a, player_b, roll_die = None):
		roll_die = roll_die or self.roll_die()
		state = (0, 0, 0, 0)

		while True:
			if state[1] >= self.__goal: return player_a
			if state[2] >= self.__goal: return player_b

			next_action = player_a(state) if state[0] == 0 else player_b(state)

			if 'roll' == next_action: state = self.roll(state, next(roll_die))
			elif 'hold' == next_action: state = self.hold(state)
			else: raise ValueError('Illegal action {}'.format(next_action))





def test():
	
	pig = Pig()


	# test hold, roll.
	assert pig.hold((1, 10, 20, 7))    == (0, 20, 17, 0)
	assert pig.hold((0, 5, 15, 10))    == (1, 15, 15, 0)
	assert pig.roll((1, 10, 20, 7), 1) == (0, 20, 11, 0)

	result = pig.roll((0, 5, 15, 10), 5)
	assert result == (0, 5, 15, 15), ('result', result)


	# test strategy_clueless.
	assert pig.strategy_clueless(None) in pig.get_actions()


	# test hold_at.
	assert pig.hold_at_factory(30)((1, 29, 15, 20)) == 'roll'
	assert pig.hold_at_factory(30)((1, 29, 15, 21)) == 'hold'
	assert pig.hold_at_factory(15)((0, 2, 30, 10))  == 'roll'
	assert pig.hold_at_factory(15)((0, 2, 30, 15))  == 'hold'


	# test play.
	def always_roll(state):
		return 'roll'

	def always_hold(state):
		return 'hold'

	for _ in range(10):
		winner = pig.play(always_hold, always_roll)
		assert winner.__name__ == 'always_roll', winner.__name__


	# test max_wins.
	assert(pig.max_wins((1, 5, 34, 4)))   == "roll"
	assert(pig.max_wins((1, 18, 27, 8)))  == "roll"
	assert(pig.max_wins((0, 23, 8, 8)))   == "roll"

	result = (pig.max_wins((0, 31, 22, 9)))
	assert result == "hold", ('result', result)

	assert(pig.max_wins((1, 11, 13, 21))) == "roll"
	assert(pig.max_wins((1, 33, 16, 6)))  == "roll"
	assert(pig.max_wins((1, 12, 17, 27))) == "roll"
	assert(pig.max_wins((1, 9, 32, 5)))   == "roll"
	assert(pig.max_wins((0, 28, 27, 5)))  == "roll"
	assert(pig.max_wins((1, 7, 26, 34)))  == "hold"
	assert(pig.max_wins((1, 20, 29, 17))) == "roll"
	assert(pig.max_wins((0, 34, 23, 7)))  == "hold"
	assert(pig.max_wins((0, 30, 23, 11))) == "hold"
	assert(pig.max_wins((0, 22, 36, 6)))  == "roll"
	assert(pig.max_wins((0, 21, 38, 12))) == "roll"
	assert(pig.max_wins((0, 1, 13, 21)))  == "roll"
	assert(pig.max_wins((0, 11, 25, 14))) == "roll"
	assert(pig.max_wins((0, 22, 4, 7)))   == "roll"
	assert(pig.max_wins((1, 28, 3, 2)))   == "roll"
	assert(pig.max_wins((0, 11, 0, 24)))  == "roll"


	return 'tests pass'	





if __name__ == '__main__':
	print test()