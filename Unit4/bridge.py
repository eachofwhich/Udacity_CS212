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
    """Return a dict of {state:action} pairs. A state is a (here, there, t) tuple,
    where here and there are frozensets of people (indicated by their times) and/or
    the 'light', and t is a number indicating the elapsed time. Action is represented
    as a tuple (person1, person2, arrow), where arrow is '->' for here to there and 
    '<-' for there to here."""
    here, there, t = state
    
    result = {}
    
    # add a state per each of the people on the side with light crossing over.
    # get combinations of two elements from the side that has ligh.
    # add state for each
    
    source, destination = (here, there) if 'light' in here else (there, here)
    arrow = '->' if source is here else '<-'
    light_set = set(['light'])
    
    

    def get_all_diffs(people, exclude = None, people_per_action = 2):
        """Return all possible combinations of people per one action."""

        exclude = exclude or None

        all_diffs = set( (person,) for person in people if person not in exclude)

        from itertools import combinations;
        pairs = set(combinations( [person for person in people if person not in exclude], people_per_action))
        
        all_diffs = all_diffs | pairs

        return all_diffs



    all_diffs = get_all_diffs(source, exclude = ['light'])


    for diff in all_diffs:

        new_source = frozenset( source - (set(diff) | light_set) )
        new_destination = frozenset( destination | set(diff) | light_set)
        time = max(diff) + t

        person1, person2 = (diff[0], diff[0]) if len(diff) < 2 else (diff[0], diff[1])
        new_here, new_there  = (new_source, new_destination) if source is here else (new_destination, new_source)
        new_state = (new_here, new_there, time)
        new_action = (person1, person2, arrow)

        result[new_state] = new_action


    return result
    
                    
    
    
        
    
    

def test():

    result = bsuccessors((frozenset([1, 'light']), frozenset([]), 3))
    assert result == {(frozenset([]), frozenset([1, 'light']), 4): (1, 1, '->')}, ('result:', result)


    result = bsuccessors((frozenset([]), frozenset([2, 'light']), 0))
    assert result =={(frozenset([2, 'light']), frozenset([]), 2): (2, 2, '<-')}, ('result', result)
    
    return 'tests pass'

print test()