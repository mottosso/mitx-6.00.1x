"""COUNTING BOBS"""

def count_bob(s):
	"""Return number of occurrences of `bob`

	Including partial occurrences, like "bobob" which is 2.

	"""

	count = 0
	for i in xrange(max(0, len(s) - 2)):
	  count += s[i:i + 3] == 'bob'
	print 'The number of times bob occurs is: %i' % count
	return count

if __name__ == '__main__':
	assert count_bob('kzbzbobbsobooqvybopoba') == 1
	assert count_bob('bobbobobowobobvwbobobxbqbobbnwdgcobobofobob') == 9
	assert count_bob('obobobobzoobmobooobobbobbbobboboounobookuoboo') == 7
