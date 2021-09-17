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

def sprout_leaves(t, leaves):
	pass

def count_leaves(tree):
	branch_counts = []
	def recursion(tree):
		if is_leaf(tree):
			return [5,6]
		for b in branches(tree):
			branch_counts.append(recursion(b))
	recursion(tree)
	return branch_counts
      

scrat = tree('berry')
sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])
numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
t = tree(1, [tree('berry',[tree('not berry')])])

print(count_leaves(sproul))
