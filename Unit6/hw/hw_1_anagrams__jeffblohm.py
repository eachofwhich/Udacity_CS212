# -----------------
# User Instructions
# 
# This homework deals with anagrams. An anagram is a rearrangement 
# of the letters in a word to form one or more new words. 
#
# Your job is to write a function anagrams(), which takes as input 
# a phrase and an optional argument, shortest, which is an integer 
# that specifies the shortest acceptable word. Your function should
# return a set of all the possible combinations of anagrams. 
#
# Your function should not return every permutation of a multi word
# anagram: only the permutation where the words are in alphabetical
# order. For example, for the input string 'ANAGRAMS' the set that 
# your function returns should include 'AN ARM SAG', but should NOT 
# include 'ARM SAG AN', or 'SAG AN ARM', etc...

from functools import update_wrapper


def decorator(d):
    def _d(fn):
        return update_wrapper(d(fn), fn)
    return update_wrapper(_d, d)



@decorator
def memo(fn):
    cache = {}

    def decorated(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = fn(*args)
            return result
        except ValueError:
            return fn(*args)

    return decorated











@memo
def find_words(letters):
    return extend_prefix('', letters, set())

def extend_prefix(pre, letters, results):
    # letters are pre-sorted, so it becomes easy not to extend the same
    # letter at the same level more than once
    if pre in WORDS: results.add((pre,letters))  # save letters too!  then use this instead of replacing later
    if pre in PREFIXES:
        pletter = None
        for L in letters:
            if L != pletter:
                extend_prefix(pre+L, letters.replace(L, '', 1), results)
                pletter = L            
    return results

def prefixes(word):
    "A list of the initial sequences of a word, not including the complete word."
    return [word[:i] for i in range(len(word))]

def readwordlist(filename):
    "Return a pair of sets: all the words in a file, and all the prefixes. (Uppercased.)"
    wordset = frozenset(open(filename).read().upper().split())
    prefixset = frozenset(p for word in wordset for p in prefixes(word))
    return wordset, prefixset

WORDS, PREFIXES = readwordlist('words4k.txt')

@memo
def xanagrams(phrase, prevword, shortest=2):
    """Return a set of phrases with words from WORDS that form anagram
    of phrase. Spaces can be anywhere in phrase or anagram. All words 
    have length >= shortest. Phrases in answer must have words in 
    lexicographic order (not all permutations)."""

    plen = len(phrase)  
    if plen < shortest:
        return set()
    words = [(word,extra) for (word,extra) in find_words(phrase)]
    result = set()    
    for (word,extra) in words:        
        wordlen = len(word)        
        if wordlen < shortest or word < prevword:
            continue
        if wordlen == plen:
            result.add(word)
        else:     
            for ritem in xanagrams(extra,word,shortest):
                result.add(word + ' ' + ritem)
    return result

def anagrams(phrase, shortest=2):
    phrase = "".join(sorted(phrase.replace(' ','')))
    return xanagrams(phrase,'',shortest)



    



# ------------
# Helpful functions
# 
# You may find the following functions useful. These functions
# are identical to those we defined in lecture. 

def removed(letters, remove):
    "Return a str of letters, but with each letter in remove removed once."
    for L in remove:
        letters = letters.replace(L, '', 1)
    return letters







# ------------
# Testing
# 
# Run the function test() to see if your function behaves as expected.

def test():

    result = anagrams('TORCHWOOD')
    assert 'DOCTOR WHO' in result, result

    assert 'BOOK SEC TRY' in anagrams('OCTOBER SKY')
    assert 'SEE THEY' in anagrams('THE EYES')
    assert 'LIVES' in anagrams('ELVIS')

    result = anagrams('PYTHONIC')
    assert result == set([
        'NTH PIC YO', 'NTH OY PIC', 'ON PIC THY', 'NO PIC THY', 'COY IN PHT',
        'ICY NO PHT', 'ICY ON PHT', 'ICY NTH OP', 'COP IN THY', 'HYP ON TIC',
        'CON PI THY', 'HYP NO TIC', 'COY NTH PI', 'CON HYP IT', 'COT HYP IN',
        'CON HYP TI']), result

    return 'tests pass'

print test()

