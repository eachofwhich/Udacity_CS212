# Unit 3 Hw 3-3
# Implement a function findtags() that extracts all HTML tags from a document.

import sys, re





def findtags(text):
	"""Return a list of all HTML tags within text."""

	pattern_string = r'<\s*\w+(?:\s*\w+\s*="?[\w\.\_]+"?)*\s*>'
	regex = re.compile(pattern_string)

	return regex.findall(text)
	



testtext1 = """
My favorite website in the world is probably 
<a href="www.udacity.com">Udacity</a>. If you want 
that link to open in a <b>new tab</b> by default, you should
write <a href="www.udacity.com"target="_blank">Udacity</a>
instead!
"""

testtext2 = """
Okay, so you passed the first test case. <let's see> how you 
handle this one. Did you know that 2 < 3 should return True? 
So should 3 > 2. But 2 > 3 is always False.
"""

testtext3 = """
It's not common, but we can put a LOT of whitespace into 
our HTML tags. For example, we can make something bold by
doing <         b           > this <   /b    >, Though I 
don't know why you would ever want to.
"""

def test():
	result = findtags(testtext1)
	check = ['<a href="www.udacity.com">', '<b>', '<a href="www.udacity.com"target="_blank">']
	assert result == check, result
	                               
	assert findtags(testtext2) == []
	assert findtags(testtext3) == ['<         b           >']
	return 'tests pass'



print test()