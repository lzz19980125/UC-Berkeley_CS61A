def tree(root_label, branches=[]):
	for branch in branches:
		assert is_tree(branch), 'branches must be trees'
	return [root_label] + list(branches)

def label(tree):
        return tree[0]

def branches(tree):
        return tree[1:]

def is_leaf(tree):
        return not branches(tree)

def is_tree(tree):
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True

def print_tree(t, indent=0):
	print('  ' * indent + str(label(t)))
	for b in branches(t):
		print_tree(b, indent + 1)

def berry_finder(t):
	if (label(t) == 'berry'):
		return True
	for i in branches(t):
		berry_finder(i)
	return False



#熟练使用tree ADT

for i,j in zip(tree(1,[tree(2),tree(3)]),tree(2,[tree(3),tree(4)])):
	print((i,j))















