# Algorithm P implementation.

import random





def shuffle(deck):
    """Shuffle and return a copy of deck."""

    result, length = deck[:], len(deck)


    # go through each element and swap it with any other element
    for element in range(length - 1):
        swap(result, element, random.randrange(element, length))

    return result



def swap(deck, i, j):
    deck[i], deck[j] = deck[j], deck[i]



def test():
    collection = [element for element in range(0, 10)]
    shuffled_collection = shuffle(collection)

    assert set(shuffled_collection) == set(collection) and shuffled_collection != collection, "{} should not match {}".format(shuffled_collection, collection)



if "__main__" == __name__:
    test()

