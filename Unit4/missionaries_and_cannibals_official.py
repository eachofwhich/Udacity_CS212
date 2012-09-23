# -----------------
# User Instructions
# 
# Write a function, csuccessors, that takes a state (as defined below) 
# as input and returns a dictionary of {state:action} pairs. 
#
# A state is a tuple with six entries: (M1, C1, B1, M2, C2, B2), where 
# M1 means 'number of missionaries on the left side.'
#
# An action is one of the following ten strings: 
#
# 'MM->', 'MC->', 'CC->', 'M->', 'C->', '<-MM', '<-MC', '<-M', '<-C'
# where 'MM->' means two missionaries travel to the right side.
# 
# We should generate successor states that include more cannibals than
# missionaries, but such a state should generate no successors.

def csuccessors(state):
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""
    M1, C1, B1, M2, C2, B2 = state
    
    if M1 < C1 or M2 < C2: return {}
    
    deltas = {
                (-1, 0, -1, 1, 0, 1): 'M',
                (-2, 0, -1, 2, 0, 1): 'MM',
                (0, -1, -1, 0, 1, 1): 'C',
                (0, -2, -1, 0, 2, 1): 'CC',
                (-1, -1, -1, 1, 1, 1): 'MC',
    }



    def subtract(state1, state2):
        return tuple( 
                    map(
                        lambda x: x if x >= 0 else 0, 
                        ( state1[i] + state2[i] for i in xrange(len(state1)) )
                        )
                    )

    def add(state1, state2):
        return subtract(state1, state2[3:] + state2[:3])



    if B1:
        return dict(
                    ( (subtract(state, delta)), (action + '->') )
                    for delta, action in deltas.items()
            )

    else:
        return dict(
                    ( add(state, delta), '<-' + action )
                    for delta, action in deltas.items()
            )





def mc_problem_official(start=(3, 3, 1, 0, 0, 0), goal=None):
    """Solve the missionaries and cannibals problem.
    State is 6 ints: (M1, C1, B1, M2, C2, B2) on the start (1) and other (2) sides.
    Find a path that goes from the initial state to the goal state (which, if
    not specified, is the state with no people or boats on the start side."""
    if goal is None:
        goal = (0, 0, 0) + start[:3]
    if start == goal:
        return [start]
    explored = set() # set of states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in csuccessors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if state == goal:
                    return path2
                else:
                    frontier.append(path2)
    return []





def mc_problem( start = (3, 3, 1, 0, 0, 0), goal = None):
    goal = goal or (0, 0, 0) + start[:3]

    explored = set()
    to_explore = [[start]]

    if start == goal: return [start]


    while to_explore:

        path = to_explore.pop(0)
        last_state = path[-1]

        # print 'to_explore: %s, path: %s' % (to_explore, path)

        for successor, action in csuccessors(last_state).items():

            if successor in explored:
                # print 'already explored %s, skipping.' % str(successor)
                continue

            explored.add(successor)

            new_path = path + [action, successor]

            if successor == goal: return new_path

            # print 'successor: %s, action: %s, goal: %s' % (successor, action, goal)

            to_explore.append(new_path)


    return []







def test():


    print mc_problem((4, 3, 1, 0, 0, 0))



    result = csuccessors((2, 2, 1, 0, 0, 0))
    assert result == {(2, 1, 0, 0, 1, 1): 'C->', 
                                               (1, 2, 0, 1, 0, 1): 'M->', 
                                               (0, 2, 0, 2, 0, 1): 'MM->', 
                                               (1, 1, 0, 1, 1, 1): 'MC->', 
                                               (2, 0, 0, 0, 2, 1): 'CC->'}, ('result', result)


    result = csuccessors((1, 1, 0, 4, 3, 1))
    assert result == {(1, 2, 1, 4, 2, 0): '<-C', 
                       (2, 1, 1, 3, 3, 0): '<-M', 
                       (3, 1, 1, 2, 3, 0): '<-MM', 
                       (1, 3, 1, 4, 1, 0): '<-CC', 
                       (2, 2, 1, 3, 2, 0): '<-MC'}, ('result', result)



    result = csuccessors((1, 4, 1, 2, 2, 0))
    assert result == {}, ('result', result)
    return 'tests pass'

print test()