# Unit 4-4




Fail = []



def pour_problem(X, Y, goal, start = (0, 0)):
	""""""
	if goal in start: return [start]

	explored = set()
	frontier = [[start]] #[paths]

	while frontier:
		path = frontier.pop(0)
		x, y = path[-1] # The last element of the path is the current state.

		for state, action in successors(x, y, X, Y).items():

			if state not in explored:

				path2 = path + [action, state]
				explored.add(state)	

				if goal in state:
					return path2
				else:
					frontier.append(path2)

	return Fail
					


def successors(x, y, X, Y):
	
	assert x <= X and y <= Y, (x, y)

	return {
				(X, y): 'Fill X',
				(x, Y): 'Fill Y',
				(0, y): 'Empty X',
				(x, 0): 'Empty Y',
				( (0, x + y) if Y >= x + y else (x - (Y - y), Y) ): 'X -> Y',
				( (x + y, 0) if X >= x + y else ( X, y - (X - x)) ): 'Y -> X',
	}





def test():
	print pour_problem(4, 9, 6, (0, 0))



if __name__ == '__main__':
	test()