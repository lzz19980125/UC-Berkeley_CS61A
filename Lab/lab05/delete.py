def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
	    assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
	    return False
    for branch in branches(tree):
	    if not is_tree(branch):
		    return False
    return True

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def is_leaf(tree):
    return not branches(tree)

def copy_tree(t):
	return tree(label(t), [copy_tree(b) for b in branches(t)])

def print_tree(t, indent=0):
	print('  ' * indent + str(label(t)))
	for b in branches(t):
		print_tree(b, indent + 1)

# def sprout_leaves(t, leaves):
# 	def recursion(t):
# 		if ( not is_tree(t)):
# 			return
# 		if(is_leaf(t)):
# 			t = tree(t,[leaves])
# 			return
# 		return recursion(label(t))+recursion(branches(t))
# 	for i in branches(t):
# 		recursion(i)
# 	return t




def sprout_leaves(t,leaves):
	if(is_leaf(t)):
		return t
	for i in branches(t):
		i = tree(sprout_leaves(i,leaves),[tree(i) for i in leaves])
	return t

def berry_finder(t):
	if (label(t)=='berry'):
		return True
	for i in branches(t):
		return berry_finder(i)
	return False

def recursion(n,m):
	if (m==1 or m==0):
		return 1
	if(n-m>m):
		return recursion(n-m,m)+recursion(n,m-1)
	else:
		return recursion(n-m,n-m) +recursion(n,m-1)


print(recursion(10,8))
