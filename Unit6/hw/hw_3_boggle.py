# -----------------
# User Instructions
# 
# In this problem, you will define a function, boggle_words(), 
# that takes a board as input and returns a set of words that
# can be made from the board according to the rules of Boggle.

def boggle_words(board, minlength=3):
    """
    board
    words
    prefixes
    border
    neighbors
    """
    board_size = size(board)


    def find_words(board, current_word, current_index, result = None, used = None):
        used = used if used is not None else set()
        result = result if result is not None else set()

        if current_word[-1] == BORDER: return set()

        if current_index in used: return set()
        used = used | set([current_index])

        if current_word in WORDS and minlength <= len(current_word):
            result.add(current_word)
            used.add(current_index)

        if current_word not in PREFIXES: return set()

        for neighbor in neighbors(current_index, board_size):
            find_words(board, current_word + board[neighbor], neighbor, result, used)

        return result




    return set( word for index, letter in enumerate(board) 
                for word in find_words(board, letter, index) )

    


def test():
    b = Board('XXXX TEST XXXX XXXX')
    assert b == '|||||||XXXX||TEST||XXXX||XXXX|||||||'
    assert display(b) == """
||||||
|XXXX|
|TEST|
|XXXX|
|XXXX|
||||||""".strip()

    result = boggle_words(b)
    print result
    assert result == set(['SET', 'SEX', 'TEST'])

    assert neighbors(20, 6) == (13, 14, 15, 19, 21, 25, 26, 27)
    assert len(boggle_words(Board('TPLER ORAIS METND DASEU NOWRB'))) == 317
    assert boggle_words(Board('PLAY THIS WORD GAME')) == set([
        'LID', 'SIR', 'OAR', 'LIS', 'RAG', 'SAL', 'RAM', 'RAW', 'SAY', 'RID', 
        'RIA', 'THO', 'HAY', 'MAR', 'HAS', 'AYS', 'PHI', 'OIL', 'MAW', 'THIS', 
        'LAY', 'RHO', 'PHT', 'PLAYS', 'ASIDE', 'ROM', 'RIDE', 'ROT', 'ROW', 'MAG', 
        'THIRD', 'WOT', 'MORE', 'WOG', 'WORE', 'SAID', 'MOR', 'SAIL', 'MOW', 'MOT', 
        'LAID', 'MOA', 'LAS', 'MOG', 'AGO', 'IDS', 'HAIR', 'GAME', 'REM', 'HOME', 
        'RED', 'WORD', 'WHA', 'WHO', 'WHOM', 'YID', 'DRAW', 'WAG', 'SRI', 'TOW', 
        'DRAG', 'YAH', 'WAR', 'MED', 'HIRE', 'TOWARDS', 'ORS', 'ALT', 'ORE', 'SIDE', 
        'ALP', 'ORA', 'TWA', 'ERS', 'TOR', 'TWO', 'AIS', 'AIR', 'AIL', 'ERA', 'TOM', 
        'AID', 'TOG', 'DIS', 'HIS', 'GAR', 'GAM', 'HID', 'HOG', 'PLAY', 'GOA', 'HOW', 
        'HOT', 'WARM', 'GOT', 'IRE', 'GOR', 'ARS', 'ARM', 'ARE', 'TOWARD', 'THROW'])    
    return 'tests pass'

    
def Board(text):
    """Input is a string of space-separated rows of N letters each;
    result is a string of size (N+2)**2 with borders all around."""
    rows = text.split()
    N = len(rows)
    rows = [BORDER*N] + rows + [BORDER*N]
    return ''.join(BORDER + row + BORDER for row in rows)

def size(board): return int(len(board)**0.5)

def neighbors(i, N):
    return (i-N-1, i-N, i-N+1, i-1, i+1, i+N-1, i+N, i+N+1)

BORDER = '|'

def display(board):
    "Return a string representation of board, suitable for printing."
    N = size(board)
    return '\n'.join(board[i:i+N] for i in range(0, N**2, N))

# ------------
# Helpful functions
# 
# You may find the following functions useful. These functions
# are identical to those we defined in lecture. 

def prefixes(word):
    "A list of the initial sequences of a word, not including the complete word."
    return [word[:i] for i in range(len(word))]

def readwordlist(filename):
    "Return a pair of sets: all the words in a file, and all the prefixes. (Uppercased.)"
    wordset = set(open(filename).read().upper().split())
    prefixset = set(p for word in wordset for p in prefixes(word))
    return wordset, prefixset

WORDS, PREFIXES = readwordlist('words4k.txt')

print test()

