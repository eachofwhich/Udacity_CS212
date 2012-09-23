"""
UNIT 2: Logic Puzzle

You will write code to solve the following logic puzzle:

1. The person who arrived on Wednesday bought the laptop.
2. The programmer is not Wilkes.
3. Of the programmer and the person who bought the droid,
   one is Wilkes and the other is Hamming. 
4. The writer is not Minsky.
5. Neither Knuth nor the person who bought the tablet is the manager.
6. Knuth arrived the day after Simon.
7. The person who arrived on Thursday is not the designer.
8. The person who arrived on Friday didn't buy the tablet.
9. The designer didn't buy the droid.
10. Knuth arrived the day after the manager.
11. Of the person who bought the laptop and Wilkes,
    one arrived on Monday and the other is the writer.
12. Either the person who bought the iphone or the person who bought the tablet
    arrived on Tuesday.

You will write the function logic_puzzle(), which should return a list of the
names of the people in the order in which they arrive. For example, if they
happen to arrive in alphabetical order, Hamming on Monday, Knuth on Tuesday, etc.,
then you would return:

['Hamming', 'Knuth', 'Minsky', 'Simon', 'Wilkes']

(You can assume that the days mentioned are all in the same week.)
"""

from itertools import permutations



def logic_puzzle():
	"Return a list of the names of the people, in the order they arrive."

	orderings = list(permutations((1, 2, 3, 4, 5)))
	mon, tue, wed, thur, fri = 1, 2, 3, 4, 5

	result = next(
				(hamming, knuth, minsky, simon, wilkes)

			
			for (hamming, knuth, minsky, simon, wilkes) in orderings
				if knuth - simon == 1

			for _, programmer, writer, manager, designer in orderings
				if programmer is not wilkes
				and writer is not minsky
				and knuth is not manager
				and thur is not designer
				and knuth - manager == 1
				and ( wilkes is mon or wilkes is writer )


			for _, laptop, droid, tablet, iphone in orderings
				if wed is laptop
				and ( wilkes is programmer or wilkes is droid )
				and ( hamming is programmer or hamming is droid )
				and tablet is not manager
				and fri is not tablet
				and designer is not droid
				and ( laptop is mon or laptop is writer )
				and ( iphone is tue or tablet is tue )	
		)

	hamming, knuth, minsky, simon, wilkes = result
	people = {hamming: 'Hamming', knuth: 'Knuth', minsky: 'Minsky', simon: 'Simon', wilkes: 'Wilkes'}
	return [people[day] for day in xrange(1, 6)]






def test():
	result = logic_puzzle()
	assert ['Wilkes', 'Simon', 'Knuth', 'Hamming', 'Minsky'] == result, result
	print 'All good.'



test()




