# Homework 3-2
from functools import update_wrapper





def decorator(dec):
	
	def decorate(fn):
		return update_wrapper(dec(fn), fn)

	return update_wrapper(decorate, dec)



def sqrt(x):
	return x*x



@decorator
def inverse(fn, delta = 1/128.):

	def new_fn(x):

		tracker = x / 2

		while fn(tracker) > x:
			tracker = tracker / 2
			#This makes this function slower approximately by a factor of 7.
			# if fn(tracker) < x:
			# 	tracker = tracker + (tracker/2)

		while x > fn(tracker):
			tracker += delta

		return tracker if fn(tracker) - x < x - fn(tracker - delta) else tracker - delta

	return new_fn



def test():
	
	sqrt_inverse = inverse(sqrt)
	print(sqrt_inverse(1000000000))



if __name__ == '__main__':
	test()