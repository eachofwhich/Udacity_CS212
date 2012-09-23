# -----------------
# User Instructions
# 
# write a function, bsuccessors2 that takes a state as input
# and returns a dictionary of {state:action} pairs.
# 
# The new representation for a path should be a list of 
# [state, (action, total time), state, ... , ], though this 
# function will just return {state:action} pairs and will
# ignore total time. 
#
# The previous bsuccessors function is included for your reference.

def bsuccessors2(state):
    """Return a dict of {state:action} pairs. A state is a
    (here, there) tuple, where here and there are frozensets
    of people (indicated by their travel times) and/or the light."""
    
    here, there = state

    if 'light' in here:

        return dict(
                        (
                            (
                                frozenset(here - set([a, b, 'light'])),
                                frozenset(there | set([a, b, 'light']))
                            ), 
                                (a, b, '->')
                        )

                        for a in here if 'light' != a
                        for b in here if 'light' != b
            )

    else:

        return dict(
                        (
                            (
                                frozenset(there - set([a, b, 'light'])),
                                frozenset(here | set([a, b, 'light'])),
                            ), 
                            (a, b, '<-')
                        )

                        for a in there if 'light' != b
                        for b in there if 'light' != b
                    )






def test():
    here1 = frozenset([1, 'light']) 
    there1 = frozenset([])

    here2 = frozenset([1, 2, 'light'])
    there2 = frozenset([3])
    
    assert bsuccessors2((here1, there1)) == {
            (frozenset([]), frozenset([1, 'light'])): (1, 1, '->')}
    assert bsuccessors2((here2, there2)) == {
            (frozenset([1]), frozenset(['light', 2, 3])): (2, 2, '->'), 
            (frozenset([2]), frozenset([1, 3, 'light'])): (1, 1, '->'), 
            (frozenset([]), frozenset([1, 2, 3, 'light'])): (2, 1, '->')}
    return 'tests pass'
print test()