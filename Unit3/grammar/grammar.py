# Unit 3-33
# An implementation of a simple grammar parser.





def grammar(string, whitespace = r'\s*'):
	"""Parse string and return a grammar dict."""

	result = {' ': whitespace}

	for line in string.split('\n'):
		if '' == line.strip(): continue

		left, right = line.strip().split('=>')
		alternatives = right.strip().split('|')

		definitions = tuple(alt.split() for alt in alternatives)
		result[left] = definitions

	return result



def parse(symbol, text, G):
	""""""
	