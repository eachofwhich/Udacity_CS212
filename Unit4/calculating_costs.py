# -----------------
# User Instructions
# 
# Write a function, path_cost, which takes a path as input 
# and returns the total cost associated with that path. 
# Remember that paths will obey the convention
# path = [state, (action, total_cost), state, ...] 
#
# If a path is less than length 3, your function should
# return a cost of 0.

def path_cost(path):
    """The total cost of a path (which is stored in a tuple
    with the final action."""
    # path = [state, (action, total_cost), state, ... ]
    offset = -1 if not len(path) % 2 else -2
    return path[offset][1]


        
def bcost(action):
    """Returns the cost (a number) of an action in the
    bridge problem."""
    # An action is an (a, b, arrow) tuple; a and b are 
    # times; arrow is a string. 
    a, b, arrow = action
    return max(a, b)



def test():

    result = path_cost(('fake_state1', ((2, 5, '->'), 5), 'fake_state2'))
    assert result == 5, ('result', result)


    result = path_cost(('fs1', ((2, 1, '->'), 2), 'fs2', ((3, 4, '<-'), 6), 'fs3'))
    assert result == 6, ('result', result)


    assert bcost((4, 2, '->'),) == 4
    assert bcost((3, 10, '<-'),) == 10
    return 'tests pass'

print test()