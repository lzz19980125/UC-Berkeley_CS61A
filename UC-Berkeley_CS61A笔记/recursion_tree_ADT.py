def tree(label, branches=[]):
	for branch in branches:
		assert is_tree(branch), 'branches must be trees'
	return [label] + list(branches)

def label(tree):
	return tree[0]

def branches(tree):
	return tree[1:]

def is_tree(tree):
	if type(tree) != list or len(tree) < 1:
		return False
	for branch in branches(tree):
		if not is_tree(branch):
			return False
	return True

def is_leaf(tree):
	return not branches(tree)

def insertBranches(t,b):
	def recursion(t):
		if (is_leaf(t)):
			t = tree(t,b)
			return
		return recursion(branches(t))
	for i in branches(t):
		recursion(i)
	return t

def getRootVal(tree):
	pass

def getLeftChild(tree):
	pass

def getRightChild(tree):
	pass

sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])
t = insertBranches(sproul,[5,6])
print(t)