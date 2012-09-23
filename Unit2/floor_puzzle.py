#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.





import itertools





def floor_puzzle():
    
    # Concepts: people, floors, adjacent, upper, bottom, higher floor
    top, bottom = 5, 1
    
    permutations = itertools.permutations([1, 2, 3, 4, 5])
    (Hopper, Kay, Liskov, Perlis, Ritchie) = next((Hopper, Kay, Liskov, Perlis, Ritchie) 
    			for (Hopper, Kay, Liskov, Perlis, Ritchie) in permutations 
                if Hopper is not top and Kay is not bottom and Liskov not in (top, bottom) 
                and higher(Perlis, Kay) and not adjacent(Ritchie, Liskov) and not adjacent(Liskov, Kay)
                )
    
    return [Hopper, Kay, Liskov, Perlis, Ritchie]



def higher(a, b):
	return a > b



def adjacent(a, b):
	return 1 == abs(a - b)



def test():
	solution = floor_puzzle()
	print solution



if __name__ == '__main__':
	test()