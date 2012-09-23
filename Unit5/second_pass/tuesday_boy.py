# Tuesday Boys. Unit 5-28

from itertools import product


def tuesday_boys():
	
	sexes = 'BG'
	week = 'SMTWtFs'
	one_boy = 'BT'

	all_possibilities = [ sex1 + day1 + sex2 + day2 
						for sex1 in sexes for day1 in week 
						for sex2 in sexes for day2 in week 
						]
	# the line below uses itertools.product, and is equivalent to the line above.
	all_possibilities = [ ''.join(possib) for possib in product(sexes, week, sexes, week) ]

	after_condition_possibilities = [possibility for possibility in all_possibilities if one_boy in possibility]

	two_boys_count = len( [possib for possib in after_condition_possibilities if possib.count('B') == 2])

	return two_boys_count, '/', len(after_condition_possibilities)



print tuesday_boys()