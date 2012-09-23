# Implements the regex matcher from Unit 3.
# Operators: lit(), star(), plus(), opt(), seq(), alt(), oneof(), dot(),
# eol()


def matchset(pattern, text):
	"""Return pattern at start of text, and return a set of remainders."""

	op, x, y = components(pattern)

	if 'lit' == op:
		return set([text[len(x):]]) if text.startswith(x) else null

	elif 'star' == op:
		return set.union( set([text]), set( 
			t2 for t1 in matchset(x, text) for t2 in matchset(pattern, t1)
			if t1 != text )
											)

	elif 'plus' == op:
		pass

	elif 'alt' == op:
		return matchset(x, text) | matchset(y, text)

	elif 'opt' == op:
		return set([text]) | matchset(x, text)

	elif 'oneof' == op:
		return set([text[1:]]) if text.startswith(x) else null

	elif 'dot' == op:
		return set([text[1:]]) if text else null

	elif 'seq' == op:
		return set( remainder2 for remainder1 in matchset(x, text)
					for remainder2 in matchset(y, remainder1)
				 )
	elif 'eol' == op:
		return set(['']) if text == '' else null

	else:
		raise ValueError('Unknown patters %s' % pattern)



def components(pattern):
	"""Decompose pattern into components. Return op, x, and y."""
	x = pattern[1] if len(pattern) > 1 else None
	y = pattern[2] if len(pattern) > 2 else None
	op = pattern[0]
	return op, x, y



def match(pattern, text):
	"""Find the longest match of pattern in the string, starting at position zero."""
	remainders = matchset(pattern, text)
	if remainders:
		shortest = min(remainders, key=len)
		return text[: len(text) - len(shortest) ]



def search(pattern, text):
	"""Return the longest match of pattern in text."""
	for i in xrange(len(text)):
		result = match(pattern, text[i:])
		if result is not None:
			return result



null = frozenset()

# Operator constructors

def lit(x): return ('lit', x)

def seq(x, y): return ('seq', x, y)

def alt(x, y): return ('alt', x, y)

def star(x): return ('star', x)

def plus(x): return ('seq', x, ('star', x))

def opt(x): return alt(lit(''), x)

def oneof(chars): return ('oneof', tuple(chars))

dot = ('dot',)
eol = ('eol',)



def test():

	result = matchset(('lit', 'abc'), 'abcdef')
	assert result == set(['def']), result

	assert matchset(('seq', ('lit', 'hi '),
	                 ('lit', 'there ')), 
	               'hi there nice to meet you')          == set(['nice to meet you'])
	assert matchset(('alt', ('lit', 'dog'), 
	                ('lit', 'cat')), 'dog and cat')      == set([' and cat'])
	assert matchset(('dot',), 'am i missing something?') == set(['m i missing something?'])
	assert matchset(('oneof', 'a'), 'aabc123')           == set(['abc123'])
	assert matchset(('eol',),'')                         == set([''])
	assert matchset(('eol',),'not end of line')          == frozenset([])
	assert matchset(('star', ('lit', 'hey')), 'heyhey!') == set(['!', 'heyhey!', 'hey!'])

	assert lit('abc')         == ('lit', 'abc')
	assert seq(('lit', 'a'), 
	           ('lit', 'b'))  == ('seq', ('lit', 'a'), ('lit', 'b'))
	assert alt(('lit', 'a'), 
	           ('lit', 'b'))  == ('alt', ('lit', 'a'), ('lit', 'b'))
	assert star(('lit', 'a')) == ('star', ('lit', 'a'))
	assert plus(('lit', 'c')) == ('seq', ('lit', 'c'), 
	                              ('star', ('lit', 'c'))), plus(('lit', 'c'))
	assert opt(('lit', 'x'))  == ('alt', ('lit', ''), ('lit', 'x'))
	assert oneof('abc')       == ('oneof', ('a', 'b', 'c'))

	return 'tests pass'



if __name__ == '__main__':
	print test()