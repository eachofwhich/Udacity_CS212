# -----------------
# User Instructions
# 
# In this problem, you will solve the pouring problem for an arbitrary
# number of glasses. Write a function, more_pour_problem, that takes 
# as input capacities, goal, and (optionally) start. This function should 
# return a path of states and actions.
#
# Capacities is a tuple of numbers, where each number represents the 
# volume of a glass. 
#
# Goal is the desired volume and start is a tuple of the starting levels
# in each glass. Start defaults to None (all glasses empty).
#
# The returned path should look like [state, action, state, action, ... ]
# where state is a tuple of volumes and action is one of ('fill', i), 
# ('empty', i), ('pour', i, j) where i and j are indices indicating the 
# glass number. 



def more_pour_problem(capacities, goal, start=None):
    """The first argument is a tuple of capacities (numbers) of glasses; the
    goal is a number which we must achieve in some glass.  start is a tuple
    of starting levels for each glass; if None, that means 0 for all.
    Start at start state and follow successors until we reach the goal.
    Keep track of frontier and previously explored; fail when no frontier.
    On success return a path: a [state, action, state2, ...] list, where an
    action is one of ('fill', i), ('empty', i), ('pour', i, j), where
    i and j are indices indicating the glass number.


    State: tuple(level1, level2, level3, level4)
    """



    def is_goal(state):
        return goal in state



    def successors(state):
        """
        Actions: fill, empty, transfer
        """

        result = {}

        for i in xrange(len(state)):

            #empty
            new_state = (state[:i] + (0,) + state[i+1:])
            new_action = ('empty', i)
            result[new_state] = new_action
            # print 'added %s to result' % str(new_state)

            #fill
            new_state = (state[:i] + (capacities[i],) + state[i+1:])
            new_action = ('fill', i)
            result[new_state] = new_action
            # print 'added %s to result' % str(new_state)


            for j in xrange(len(state)):
                if j == i: continue

                a, b, A, B = state[i], state[j], capacities[i], capacities[j]

                a = 0 if B >= a + b else a - (B - b)
                b = a + b if B >= a + b else B

                # print 'a: %s, b: %s' % (a, b)

                new_state = list(state)
                new_state[i], new_state[j] = a, b
                new_state = type(state)(new_state)
                new_action = ('pour', i, j)

                result[new_state] = new_action
                # print 'added %s to result' % str(new_state)

        return result



    def search(starting_state, successors, is_goal):
        if is_goal(starting_state): return [[starting_state]]

        from collections import deque
        to_explore = deque([[starting_state]])
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



    start = start or (0,) * len(capacities)
    return search(start, successors, is_goal)

    
    








Fail = []
    
def test_more_pour():

    result = more_pour_problem((1, 2, 4, 8), 4)
    assert result == [(0, 0, 0, 0), ('fill', 2), (0, 0, 4, 0)], ('result', result)

    assert more_pour_problem((1, 2, 4), 3) == [
        (0, 0, 0), ('fill', 2), (0, 0, 4), ('pour', 2, 0), (1, 0, 3)] 


    starbucks = (8, 12, 16, 20, 24)
    assert not any(more_pour_problem(starbucks, odd) for odd in (3, 5, 7, 9))


    assert all(more_pour_problem((1, 3, 9, 27), n) for n in range(28))


    assert more_pour_problem((1, 3, 9, 27), 28) == []


    return 'test_more_pour passes'

print test_more_pour()