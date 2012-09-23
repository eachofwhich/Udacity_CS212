from regex1 import matchset as M





def test():
	"""Tests the regex1 module."""

	result = M.matchset(('lit', 'abc'), 'abcdef')
	assert result == set(['def']), result

	assert M.matchset(('seq', ('lit', 'hi '),
	                 ('lit', 'there ')), 
	               'hi there nice to meet you')          == set(['nice to meet you'])
	assert M.matchset(('alt', ('lit', 'dog'), 
	                ('lit', 'cat')), 'dog and cat')      == set([' and cat'])
	assert M.matchset(('dot',), 'am i missing something?') == set(['m i missing something?'])
	assert M.matchset(('oneof', 'a'), 'aabc123')           == set(['abc123'])
	assert M.matchset(('eol',),'')                         == set([''])
	assert M.matchset(('eol',),'not end of line')          == frozenset([])
	assert M.matchset(('star', ('lit', 'hey')), 'heyhey!') == set(['!', 'heyhey!', 'hey!'])

	# 3-?
	assert M.lit('abc')         == ('lit', 'abc')
	assert M.seq(('lit', 'a'), 
	           ('lit', 'b'))  == ('seq', ('lit', 'a'), ('lit', 'b'))
	assert M.alt(('lit', 'a'), 
	           ('lit', 'b'))  == ('alt', ('lit', 'a'), ('lit', 'b'))
	assert M.star(('lit', 'a')) == ('star', ('lit', 'a'))
	assert M.plus(('lit', 'c')) == ('seq', ('lit', 'c'), 
	                              ('star', ('lit', 'c'))), M.plus(('lit', 'c'))
	assert M.opt(('lit', 'x'))  == ('alt', ('lit', ''), ('lit', 'x'))
	assert M.oneof('abc')       == ('oneof', ('a', 'b', 'c'))


	# 3-8
	assert M.match(('star', ('lit', 'a')),'aaabcd') == 'aaa'
	assert M.match(('alt', ('lit', 'b'), ('lit', 'c')), 'ab') == None
	assert M.match(('alt', ('lit', 'b'), ('lit', 'a')), 'ab') == 'a'
	assert M.search(('alt', ('lit', 'b'), ('lit', 'c')), 'ab') == 'b'

	return 'tests pass'



if __name__ == '__main__':
	print test()
