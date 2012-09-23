# An imlementation of a decorator for decorators that preserves original function's metadata.
# CS212 Unit 3-26

from functools import update_wrapper





def decorator(dec):
	"""A decorator for decorators that preserves original function meta-data."""
	def _dec(fn):
		return update_wrapper(dec(fn), fn)

	return update_wrapper(_dec, dec)



@decorator
def wrap(fn):
	"""wrap()"""
	def decorate():
		print 'wrap'
		seq()

	return decorate



@wrap
def seq():
	"""seq()"""
	print 'seq'



if __name__ == '__main__':
	
	assert 'seq()' == seq.__doc__, 'Expected %, got %' % ('seq()', seq.__doc__)
	assert 'wrap()' == wrap.__doc__, 'Expected %, got %' % ('wrap()', wrap.__doc__)
	print 'All good.'