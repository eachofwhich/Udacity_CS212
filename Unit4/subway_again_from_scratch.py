

class Subway:

	def __init__(self, **map):
		self.__map = self.__parse_map(map)



	def get_map(self): return self.__map

	def set_goal(self, goal): self.__goal = goal



	def __parse_map(self, map):
		
		from collections import defaultdict
		result = defaultdict(dict)


		for line, stops in map.items():

			stops_list = stops.split()

			for i in xrange(len(stops_list) - 1):
				current, next = stops_list[i:i+2]
				result[current][next] = line
				result[next][current] = line


		return result



	def __search(self, start_state, successors, is_goal):
		""""""
		if is_goal(start_state): return [[start_state]]


		from collections import deque
		to_explore = deque([[start_state]])
		explored = set()


		while to_explore:

			current_path = to_explore.pop()
			current_state = current_path[-1]

			for state, action in successors(current_state).items():

				if state in explored: continue
				explored.add(state)

				new_path = current_path + [action, state]

				if is_goal(state): return new_path

				to_explore.append(new_path)


		return []



	def __successors(self, state): return self.__map[state]



	def __is_goal(self, stop):
		""""""
		return stop == self.__goal



	def find_path(self, here, there):
		""""""
		self.set_goal(there)

		result = self.__search(here, self.__successors, self.__is_goal)
		return result



	def find_line_path(self, here, there):
		""""""
		self.set_goal(there)
		all_stop_path = self.__search(here, self.__successors, self.__is_goal)

		result = all_stop_path[:1]

		for index in xrange(1, len(all_stop_path) - 3, 2):
			if index > 1 and all_stop_path[index] != all_stop_path[index - 2]:
				result.extend(all_stop_path[index: index + 2])

		result += all_stop_path[-2:]
		return result



def test():
	
	lines = dict(blue='bowdoin government state aquarium maverick airport suffolk revere wonderland',
		    orange='oakgrove sullivan haymarket state downtown chinatown tufts backbay foresthills',
		    green='lechmere science north haymarket government park copley kenmore newton riverside',
		    red='alewife davis porter harvard central mit charles park downtown south umass mattapan')

	subway = Subway(**lines)


	here_there = (
				('mattapan', 'foresthills'),
				('mit', 'government')
				)

	for here, there in here_there:
		print subway.find_path(here, there)
		print subway.find_line_path(here, there)


	print test_ride(subway)








def test_ride(subway):

	result = subway.find_path('mit', 'government')
	assert result == ['mit', 'red', 'charles', 'red', 'park', 'green', 'government'], ('result', result)


	result = subway.find_path('mattapan', 'foresthills')
	assert result == ['mattapan', 'red', 'umass', 'red', 'south', 'red', 'downtown',
	                                            'orange', 'chinatown', 'orange', 'tufts', 'orange', 'backbay', 
	                                            'orange', 'foresthills'], ('result', result)


	result = subway.find_path('newton', 'alewife')
	assert result == [
	    'newton', 'green', 'kenmore', 'green', 'copley', 'green', 'park', 'red', 'charles', 'red',
	    'mit', 'red', 'central', 'red', 'harvard', 'red', 'porter', 'red', 'davis', 'red', 'alewife'], ('result', result)


	return 'test_ride passes'






if __name__ == '__main__':
	test()