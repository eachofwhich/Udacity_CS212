# Cache decorator implementation.
# Unit 3-27

from functools import update_wrapper





def decorator(dec):
	def _dec(fn):
		return update_wrapper(dec(fn), fn)
	return update_wrapper(_dec, dec)



@decorator
def cached(fn):
	cache = {}

	def _cached(num):

		if num.__hash__ is None: return fn(num)
		if num in cache: return cache[num]

		print 'running original square()'
		result = fn(num)
		cache[num] = result
		return result

	return _cached



@cached
def square(num):
	"""square()"""
	return num**2