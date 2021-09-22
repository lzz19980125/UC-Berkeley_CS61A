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
def max_path_sum(t):
    if(is_leaf(t)):
        return 1
    for i in branches(t):
        return 1+max_path_sum(i)
    return max([1+max_path_sum(i) for i in branches(t)])


# t = tree(1,[tree(5,[tree(1),tree(3)]),tree(10)])
# print_tree(t)
# print("最大长度为："+str(max_path_sum(t)))


################################################################################################################################
 # Question 1.2
def max_path_sum(t):
    print("未完成！！！！！！！")
    pass











# t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
# print_tree(t)
######################################################################################################################################################
# Question 1.3
def square_tree(t):
    if(is_leaf(t)):
        return [label(t)**2]
    return tree(label(t)**2,[square_tree(i) for i in branches(t)])

numbers = tree(1,[tree(2,[tree(3),tree(4)]),tree(5,[tree(6,[tree(7)]),tree(8)])])
print_tree(square_tree(numbers))


######################################################################################################################################################
#Question 1.4

def find_path(tree,x):
    print("未完成！！！！！！！！！！！！！！！")
    pass


######################################################################################################################################################
#Question 2.2

def prune_binary(t, nums):
    print("未完成！！！！！！！！！！！！！！！！！！")
    pass
