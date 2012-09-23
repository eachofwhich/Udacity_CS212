# A manual list shuffle implementation.

import random





def shuffle(collection):
    result = collection[:]
    swapped = [False] * len(result)

    while not all(swapped):
        i, j = random.randint(0, len(result) - 1), random.randint(0, len(result) - 1)
        swap(result, i, j)
        swapped[i], swapped[j] = True, True

    return result



def swap(collection, i, j):
    collection[i], collection[j] = collection[j], collection[i]



def test():
    collection = [element for element in range(0, 10)]
    shuffled_collection = shuffle(collection)

    assert set(shuffled_collection) == set(collection) and shuffled_collection != collection, "{} should not match {}".format(shuffled_collection, collection)



if "__main__" == __name__:
    test()
