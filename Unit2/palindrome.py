# Find the longest palindrome in a string.





def longest_subpalindrome_slice(string):
	"""Find the minimum palindrome and expand in both directions."""

	longest_palindrome, pivot_index, string = None, 0, string[:].upper()


	# maybe this could be optimized based on known longest_palindrome?
	start, end =  find_palindrome(string, pivot_index)

	while end:

		print_state(locals())

		(start, end) = expand_palindrome(string, start, end)
		pivot_index = end
		
		if end and (not longest_palindrome or end - start > longest_palindrome[1] - longest_palindrome[0]):
			longest_palindrome = (start, end)

		start, end =  find_palindrome(string, pivot_index)

	return longest_palindrome if longest_palindrome else (0, 0)



def find_palindrome(string, offset = None):
	"""Find then next smallest palindrome: either XX or XYZ, starting at offset"""
	offset = offset if offset else 0

	start, end = None, None

	print_state(locals())

	for index, char in enumerate(string, offset):

		if len(string) > index + 1:
			if string[index] == string[index + 1]:
				return (index, index + 2)

		if 0 < index < len(string) - 1:
			substring, reversed_substring = string[index - 1: index + 2], string[index + 1:index - 2:-1]
			if substring == reversed_substring:
				return (index - 1, index + 2)


	return (start, end)



def expand_palindrome(string, start, end):
	"""Expand the palindrome in both directions and return the new start and end. ABBZBBA"""

	if 2 == end - start:
		while end < len(string) and string[end] == string[start]:
			end += 1

	while start > 0 and end < len(string) and string[start - 1] == string[end]:
		start -= 1
		end += 1

	return (start, end)



def print_state(state):
	return
	print ''
	for key in state:
		print '{}: {}'.format(key, state[key])
	print '\n\n'



def test():

	L = p = longest_subpalindrome_slice

	palindrome1 = 'ABBZBBA'
	print('{}: {}'.format(palindrome1, p(palindrome1)))

	palindrome1 = 'ABBA'
	print('{}: {}'.format(palindrome1, p(palindrome1)))

	palindrome1 = 'RACE CARR'
	print('{}: {}'.format(palindrome1, p(palindrome1)))

	assert L('racecar') == (0, 7)
	assert L('Racecar') == (0, 7)
	assert L('RacecarX') == (0, 7)
	assert L('Race carr') == (7, 9)
	assert L('') == (0, 0)
	assert L('something rac e car going') == (8,21)

	string = 'xxxxx'
	check = (0, 5)
	result = L(string)
	assert result == check, 'string: {}, result = {}, check = {}'.format(string, result, check)

	assert L('Mad am I ma dam.') == (0, 15)
	return 'tests pass'





if __name__ == '__main__':
	print(test())