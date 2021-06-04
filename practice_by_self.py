def paths(m, n):
	if ((m == 0) | (n == 0)):
		if ((m == 0) & (n == 0)):
			return 1
		elif (n != 0):
			return paths(m, n - 1)
		return paths(m - 1, n)

	return paths(m - 1, n) + paths(m, n - 1)

print(paths(2, 2))


