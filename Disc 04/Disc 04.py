def even_weighted(s):
	"""
	>>> x = [1, 2, 3, 4, 5, 6]
	>>> even_weighted(x)
	[0, 6, 20]
	"""
	return [s[i]*i for i in range(len(s)) if(i%2==0)]

x = [1,2,3,4,5,6]
print(even_weighted(x))


def max_product(s):

	"""Return the maximum product that can be formed using non-consecutiveelements of s.

	>>> max_product([10,3,1,9,2]) # 10 * 9
	90
	>>> max_product([5,10,5,10,5]) # 5 * 5 * 5
	125
	>>> max_product([])
	1
	"""

	if(s==[]):
		return 1
	return max(s[0]*max_product(s[2:]),max_product(s[1:]))




print(max_product([10,3,1,9,2]))
print(max_product([5,10,5,10,5]))
print(max_product([]))
