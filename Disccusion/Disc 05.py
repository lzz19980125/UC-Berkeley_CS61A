# Tree ADT
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

#################################################################################################################################
#  Question 1.1
# def max_path_sum(t):
# 	result = []
# 	def recursion(b):
# 		if (is_leaf(b)):
# 			return 1
# 		return (1+recursion(branches(b)))
# 	for b in branches(t):
# 		result.append(recursion(b))
# 	return max(result)
#
#
# t = tree(1,[tree(5,[tree(1),tree(3)]),tree(10)])
# print_tree(t)
# print(max_path_sum(t))


################################################################################################################################
#  Question 1.2
# def max_path_sum(t):
#
#
#
#
#
#
#
#
#
#
#
# t = tree(1,[tree(5,[tree(1),tree(3)]),tree(10)])
# print_tree(t)