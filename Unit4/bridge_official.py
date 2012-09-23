# -----------------
# User Instructions
# 
# Write a function, bsuccessors(state), that takes a state as input
# and returns a dictionary of {state:action} pairs.
#
# A state is a (here, there, t) tuple, where here and there are 
# frozensets of people (indicated by their times), and potentially
# the 'light,' t is a number indicating the elapsed time.
#
# An action is a tuple (person1, person2, arrow), where arrow is 
# '->' for here to there or '<-' for there to here. When only one 
# person crosses, person2 will be the same as person one, so the
# action (2, 2, '->') means that the person with a travel time of
# 2 crossed from here to there alone.

def bsuccessors(state):
    
    here, there, t = state

    arrow = '->' if 'light' in here else '<-'

    if 'light' in here:
        return dict(
                        ((
                        frozenset(here - set([a, b, 'light']) ),
                        frozenset(there | set([a, b, 'light'])),
                        max(a, b) + t
                        ),
                        (a, b, arrow))

                        for a in here if a != 'light'
                        for b in here if b != 'light'
                )

    else:
        return dict(
                        ((
                        frozenset(there | set([a, b, 'light']) ),
                        frozenset(here - set([a, b, 'light'])),
                        max(a, b) + t
                        ),
                        (a, b, arrow))

                        for a in there if a != 'light'
                        for b in there if b != 'light'
                )

                    
    
    
        
    
    

def test():

    result = bsuccessors((frozenset([1, 'light']), frozenset([]), 3))
    assert result == {(frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}, ('result:', result)


    result = bsuccessors((frozenset([]), frozenset([2, 'light']), 0))
    assert result =={(frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}, ('result', result)
    
    return 'tests pass'

print test()