from regex2 import matchset as M





def test():
	"""Tests the regex2 module."""

	assert M.match(M.star(M.lit('a')), 'aaaaabbbaa') == 'aaaaa'
	assert M.match(M.lit('hello'), 'hello how are you?') == 'hello'
	assert M.match(M.lit('x'), 'hello how are you?') == None

	result = M.match(M.oneof('xyz'), 'x**2 + y**2 = r**2')
	assert result == 'x'

	assert M.match(M.oneof('xyz'), '   x is here!') == None	

	return 'tests pass'



if __name__ == '__main__':
	print test()
