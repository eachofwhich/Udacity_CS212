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
    boat, no_boat = 1, 0
    
    if M1 < C1 or M2 < C2: return {}

    if B1:
        return {
                (M1 - 1, C1, no_boat, M2 + 1, C2, boat): 'M->',
                (M1 - 2, C1, no_boat, M2 + 2, C2, boat): 'MM->',
                (M1, C1 - 1, no_boat, M2, C2 + 1, boat): 'C->',
                (M1, C1 - 2, no_boat, M2, C2 + 2, boat): 'CC->',
                (M1 - 1, C1 - 1, no_boat, M2 + 1, C2 + 1, boat): 'MC->',
        }
    else:
                return {
                (M1 + 1, C1, boat, M2 - 1, C2, no_boat): '<-M',
                (M1 + 2, C1, boat, M2 - 2, C2, no_boat): '<-MM',
                (M1, C1 + 1, boat, M2, C2 - 1, no_boat): '<-C',
                (M1, C1 + 2, boat, M2, C2 - 2, no_boat): '<-CC',
                (M1 + 1, C1 + 1, boat, M2 - 1, C2 - 1, no_boat): '<-MC',
        }






def test():
    assert csuccessors((2, 2, 1, 0, 0, 0)) == {(2, 1, 0, 0, 1, 1): 'C->', 
                                               (1, 2, 0, 1, 0, 1): 'M->', 
                                               (0, 2, 0, 2, 0, 1): 'MM->', 
                                               (1, 1, 0, 1, 1, 1): 'MC->', 
                                               (2, 0, 0, 0, 2, 1): 'CC->'}

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