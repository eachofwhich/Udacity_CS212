# Experimenting with itertools.

import itertools





def test():
    
    def test_chain():
        
        l, ll, lll = [1, 2, 3], [4, 5, 6], [7, 8, 9]

        one_list = [ element for element in itertools.chain(l, ll, lll) ]
        check_list = l + ll + lll

        assert check_list == one_list, "{} should match {}".format(check_list, one_list)
        print("Great. itertools.chain() works.")


    test_chain()



if "__main__" == __name__:
    test()
