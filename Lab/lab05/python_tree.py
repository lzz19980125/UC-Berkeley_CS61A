def riffle(deck):
	return [[deck[i], deck[i + len(deck) // 2]] for i in range(len(deck) // 2)]


a = [1,2,3,4]
print([a[0],a[1]],[a[2],a[3]])