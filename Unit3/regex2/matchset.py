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
	remainders = pattern(text)
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

def lit(x): return lambda text: set([text[len(x):]]) if text.startswith(x) else null

def seq(x, y): return lambda text: set.union(*map(y, x(text)))

def alt(x, y): return lambda text: x(text) | y(text)

def star(x): return lambda text: set([text]) | set([ r2 for r1 in x(text) if r1 != text
												for r2 in star(x)(r1) ])

def plus(x): return lambda text: seq(x, star(x))

def opt(x): return lambda text: alt(lit(''), x)

def oneof(chars): return lambda text: set([text[1:]]) if text and text[0] in chars else null

dot = lambda text: set([text[1:]]) if text else null
eol = lambda text: set(['']) if text == '' else null
