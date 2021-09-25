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

# def add_trees(t1, t2):
# 	if not t1:
# 		return t2
# 	if not t2:
# 		return t1
# 	new_label = label(t1) + label(t2)
# 	t1_children, t2_children = branches(t1), branches(t2)
# 	length_t1, length_t2 = len(t1_children), len(t2_children)
# 	if length_t1 < length_t2:
# 		t1_children += [None for _ in range(length_t1, length_t2)]
# 	elif len(t1_children) > len(t2_children):
# 		t2_children += [None for _ in range(length_t2, length_t1)]
# 	return tree(new_label, [add_trees(child1, child2) for child1, child2 in zip(t1_children, t2_children)])
#
#
# numbers = tree(1,[tree(2,[tree(3),tree(4)]),tree(5,[tree(6,[tree(7)]),tree(8)])])
# print_tree(add_trees(numbers, numbers))
# print("***********************")
#
# print_tree(add_trees(tree(2), tree(3, [tree(4), tree(5)])))
# print("************************")
#
# print_tree(add_trees(tree(2, [tree(3)]), tree(2, [tree(3), tree(4)])))
# print("************************")
#
# print_tree(add_trees(tree(2, [tree(3, [tree(4), tree(5)])]),tree(2, [tree(3, [tree(4)]), tree(5)])))

def add(t1,t2):
    if(t1 == None):
        return t2
    if(t2 ==None):
        return t1
    if(is_leaf(t1) & is_leaf(t2)):
        return tree(label(t1)+label(t2))
    new_label = label(t1)+label(t2)
    t1_branches = [i for i in branches(t1)]
    t2_branches = [j for j in branches(t2)]
    if(len(t1_branches)>len(t2_branches)):
        t2_branches +=[None for i in range(len(t2_branches),len(t1_branches))]
    if(len(t1_branches)<len(t2_branches)):
        t1_branches +=[None for i in range(len(t1_branches),len(t2_branches))]
    zipper = zip(t1_branches,t2_branches)
    return tree(new_label,[add(m,n) for m,n in zipper])


numbers1 = tree(1,[tree(2),tree(3)])
print_tree(numbers1)
print("*****************************************")
numbers2 = tree(4,[tree(5)])
print_tree(numbers2)
print("*****************************************")
print_tree(add(numbers1, numbers2))







