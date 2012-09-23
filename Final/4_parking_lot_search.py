"""
UNIT 4: Search

Your task is to maneuver a car in a crowded parking lot. This is a kind of 
puzzle, which can be represented with a diagram like this: 

| | | | | | | |  
| G G . . . Y |  
| P . . B . Y | 
| P * * B . Y @ 
| P . . B . . |  
| O . . . A A |  
| O . S S S . |  
| | | | | | | | 

A '|' represents a wall around the parking lot, a '.' represents an empty square,
and a letter or asterisk represents a car.  '@' marks a goal square.
Note that there are long (3 spot) and short (2 spot) cars.
Your task is to get the car that is represented by '**' out of the parking lot
(on to a goal square).  Cars can move only in the direction they are pointing.  
In this diagram, the cars GG, AA, SSS, and ** are pointed right-left,
so they can move any number of squares right or left, as long as they don't
bump into another car or wall.  In this diagram, GG could move 1, 2, or 3 spots
to the right; AA could move 1, 2, or 3 spots to the left, and ** cannot move 
at all. In the up-down direction, BBB can move one up or down, YYY can move 
one down, and PPP and OO cannot move.

You should solve this puzzle (and ones like it) using search.  You will be 
given an initial state like this diagram and a goal location for the ** car;
in this puzzle the goal is the '.' empty spot in the wall on the right side.
You should return a path -- an alternation of states and actions -- that leads
to a state where the car overlaps the goal.

An action is a move by one car in one direction (by any number of spaces).  
For example, here is a successor state where the AA car moves 3 to the left:

| | | | | | | |  
| G G . . . Y |  
| P . . B . Y | 
| P * * B . Y @ 
| P . . B . . |  
| O A A . . . |  
| O . . . . . |  
| | | | | | | | 

And then after BBB moves 2 down and YYY moves 3 down, we can solve the puzzle
by moving ** 4 spaces to the right:

| | | | | | | |
| G G . . . . |
| P . . . . . |
| P . . . . * *
| P . . B . Y |
| O A A B . Y |
| O . . B . Y |
| | | | | | | |

You will write the function

    solve_parking_puzzle(start, N=N)

where 'start' is the initial state of the puzzle and 'N' is the length of a side
of the square that encloses the pieces (including the walls, so N=8 here).

We will represent the grid with integer indexes. Here we see the 
non-wall index numbers (with the goal at index 31):

 |  |  |  |  |  |  |  |
 |  9 10 11 12 13 14  |
 | 17 18 19 20 21 22  |
 | 25 26 27 28 29 30 31
 | 33 34 35 36 37 38  |
 | 41 42 43 44 45 46  |
 | 49 50 51 52 53 54  |
 |  |  |  |  |  |  |  |

The wall in the upper left has index 0 and the one in the lower right has 63.
We represent a state of the problem with one big tuple of (object, locations)
pairs, where each pair is a tuple and the locations are a tuple.  Here is the
initial state for the problem above in this format:
"""

puzzle1_original = (
 ('@', (31,)),
 ('*', (26, 27)), 
 ('G', (9, 10)),
 ('Y', (14, 22, 30)), 
 ('P', (17, 25, 33)), 
 ('O', (41, 49)), 
 ('B', (20, 28, 36)), 
 ('A', (45, 46)), 
 ('|', (0, 1, 2, 3, 4, 5, 6, 7, 8, 15, 16, 23, 24, 32, 39,
        40, 47, 48, 55, 56, 57, 58, 59, 60, 61, 62, 63)))

# A solution to this puzzle is as follows:

#     path = solve_parking_puzzle(puzzle1, N=8)
#     path_actions(path) == [('A', -3), ('B', 16), ('Y', 24), ('*', 4)]

# That is, move car 'A' 3 spaces left, then 'B' 2 down, then 'Y' 3 down, 
# and finally '*' moves 4 spaces right to the goal.

# Your task is to define solve_parking_puzzle:

N = 8






def get_symbol_position(state, symbol):
    for element in state:
        if symbol == element[0]: return element[1]

    raise ValueError('{} is not in the grid provided.'.format(symbol))



def is_horizontal(positions):
    if 2 > len(positions): return False
    if 1 != positions[1] - positions[0]: return False
    return True



def is_goal(state):
    car = get_symbol_position(state, '*')
    assert is_horizontal(car), 'The car must be positioned horizontally.'

    goal = get_symbol_position(state, '@')

    return car[-1] in goal



def is_position_empty(state, current, move_by):
    next_position = current + move_by

    for element in state:
        if next_position in element[1] and '@' != element[0]: return False
    return True



def new_state_changed(state, symbol, new_positions):
    state = dict(state)
    state[symbol] = new_positions
    result = tuple( (next_symbol, next_positions) for next_symbol, next_positions in state.items() )
    return result



def successors(state):
    result = {}

    for element in state:
        if element[0] in ('@', '|'): continue

        # Vertical moves.
        if not is_horizontal(element[1]):

            # North
            move_by = -N

            while is_position_empty(state, element[1][0], move_by):
                new_positions = tuple(x + move_by for x in element[1])
                new_state = new_state_changed(state, element[0], new_positions)
                new_action = (element[0], move_by)
                result[new_state] = new_action
                move_by += -N


            # South
            move_by = N

            while is_position_empty(state, element[1][-1], move_by):
                new_positions = tuple(x + move_by for x in element[1])
                new_state = new_state_changed(state, element[0], new_positions)
                new_action = (element[0], move_by)
                result[new_state] = new_action
                move_by += N



        else:

            # East.
            move_by = 1

            while is_position_empty(state, element[1][-1], move_by):
                new_positions = tuple(x + move_by for x in element[1])
                new_state = new_state_changed(state, element[0], new_positions)
                new_action = (element[0], move_by)
                result[new_state] = new_action
                move_by += 1


            # West.
            move_by = -1

            while is_position_empty(state, element[1][0], move_by):
                new_positions = tuple(x + move_by for x in element[1])
                new_state = new_state_changed(state, element[0], new_positions)
                new_action = (element[0], move_by)
                result[new_state] = new_action
                move_by += -1





    return result




def solve_parking_puzzle(start, N=N):
    """Solve the puzzle described by the starting position (a tuple 
    of (object, locations) pairs).  Return a path of [state, action, ...]
    alternating items; an action is a pair (object, distance_moved),
    such as ('B', 16) to move 'B' two squares down on the N=8 grid."""

    result = shortest_path_search(start, successors, is_goal)
    return result
















# But it would also be nice to have a simpler format to describe puzzles,
# and a way to visualize states.
# You will do that by defining the following two functions:

def locs(start, n, incr=1):
    "Return a tuple of n locations, starting at start and incrementing by incr."
    return tuple([start + incr * index for index in xrange(0, n)])


def grid(cars, N=N):
    """Return a tuple of (object, locations) pairs -- the format expected for
    this puzzle.  This function includes a wall pair, ('|', (0, ...)) to 
    indicate there are walls all around the NxN grid, except at the goal 
    location, which is the middle of the right-hand wall; there is a goal
    pair, like ('@', (31,)), to indicate this. The variable 'cars'  is a
    tuple of pairs like ('*', (26, 27)). The return result is a big tuple
    of the 'cars' pairs along with the walls and goal pairs."""

    total_length = N * N

    goal_location = N * N/2 - 1

    wall_locations = tuple(x for x in xrange(N))

    for x in xrange(N, total_length - N, N):
        border_left, border_right = x, x + N - 1
        wall_locations += (border_left, border_right) if border_right != goal_location else (border_left,)

    wall_locations += tuple(x for x in xrange(total_length - N, total_length))

    result = (('@', (goal_location,)),) + cars + (('|', wall_locations),)
    return result


def show(state, N=N):
    "Print a representation of a state as an NxN grid."
    # Initialize and fill in the board.
    board = ['.'] * N**2
    for (c, squares) in state:
        for s in squares:
            board[s] = c
    # Now print it out
    for i,s in enumerate(board):
        print s,
        if i % N == N - 1: print

# Here we see the grid and locs functions in use:

puzzle1 = grid((
    ('*', locs(26, 2)),
    ('G', locs(9, 2)),
    ('Y', locs(14, 3, N)),
    ('P', locs(17, 3, N)),
    ('O', locs(41, 2, N)),
    ('B', locs(20, 3, N)),
    ('A', locs(45, 2))))

puzzle2 = grid((
    ('*', locs(26, 2)),
    ('B', locs(20, 3, N)),
    ('P', locs(33, 3)),
    ('O', locs(41, 2, N)),
    ('Y', locs(51, 3))))

puzzle3 = grid((
    ('*', locs(25, 2)),
    ('B', locs(19, 3, N)),
    ('P', locs(36, 3)),
    ('O', locs(45, 2, N)),
    ('Y', locs(49, 3))))


# Here are the shortest_path_search and path_actions functions from the unit.
# You may use these if you want, but you don't have to.

def shortest_path_search(start, successors, is_goal):
    """Find the shortest path from start state to a state
    such that is_goal(state) is true."""
    if is_goal(start):
        return [start]
    explored = set() # set of states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        # print
        # show(s)
        for (state, action) in successors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if is_goal(state):
                    return path2
                else:
                    frontier.append(path2)
    return []

def path_actions(path):
    "Return a list of actions in this path."
    return path[1::2]









def test():

    # def x_test(value, check, expect = True):
    #     result = value == check

    #     if expect == result:
    #         print 'All good: {} == {}'.format(value, check)
    #     else:
    #         print 'Failed: {} != {}'.format(value, check)
    

    # def test_locs():
    #     x_test(locs(1, 3), (1, 2, 3))
    #     x_test(locs(1, 3, 8), (1, 9, 17))
    #     x_test(locs(26, 2), (26, 27))


    # def test_grid():
    #     x_test(puzzle1, puzzle1_original)


    # def test_get_symbol_position():
    #     x_test( get_symbol_position(puzzle1, '@'), (31,) )
    #     x_test( get_symbol_position(puzzle1, '*'), (26, 27) )


    # def test_is_horizontal():
    #     x_test(is_horizontal((22, 23)), True)


    # def test_is_goal():
    #     state = ( ('*', (30, 31)), ('@', (31,)) )
    #     x_test(is_goal(state), True)
    #     state = ( ('*', (30, 31)), ('@', (35,)) )
    #     x_test(is_goal(state), False)


    # def test_is_position_empty():
    #     state = ( ('A', (9, 17, 25)), ('B', (33, 41)) )
    #     x_test( is_position_empty(state, 33, -8), False )
    #     x_test( is_position_empty(state, 41, 8), True )


    # def test_new_state_changed():
    #     new_state = new_state_changed(puzzle1, '@', (55,))
    #     goal = get_symbol_position(new_state, '@')
    #     x_test(goal, (55,))


    # def test_successors():
    #     print puzzle1
    #     show(puzzle1)
    #     new_states = successors(puzzle1)
    #     for state in new_states:
    #         print
    #         print
    #         show(state)


    # def test_solve_parking_puzzle():
    #     result = solve_parking_puzzle(puzzle1)
    #     # print result
    #     print 'Actions:'
    #     print path_actions(result)



    # test_locs()
    # test_grid()
    # test_get_symbol_position()
    # test_is_horizontal()
    # test_is_goal()
    # test_is_position_empty()
    # test_new_state_changed()
    # test_successors()
    # test_solve_parking_puzzle()

    print path_actions(solve_parking_puzzle(puzzle1))
    print path_actions(solve_parking_puzzle(puzzle2))
    print path_actions(solve_parking_puzzle(puzzle3))



test()
