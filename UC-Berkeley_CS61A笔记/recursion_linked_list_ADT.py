empty = 'empty'
#constructor
def link(first, rest):
        """Construct a linked list from its first element and the rest."""
        assert is_link(rest), "rest must be a linked list."
        return [first, rest]
#selector
def first(s):
        """Return the first element of a linked list s."""
        assert is_link(s), "first only applies to linked lists."
        assert s != empty, "empty linked list has no first element."
        return s[0]

def rest(s):
        """Return the rest of the elements of a linked list s."""
        assert is_link(s), "rest only applies to linked lists."
        assert s != empty, "empty linked list has no rest."
        return s[1]

def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair."""
    return s == empty or (len(s) == 2 and is_link(s[1]))

#当rest部分为empty时，将此链表的长度看作1
#计算链表的长度
def len_link(s):
    if(rest(s)==empty):
        return 1
    return 1+len_link(rest(s))

#返回索引为i的链表元素
def getitem_link(s, i):
    if(i==0):
        return first(s)
    return getitem_link(rest(s),i-1)


#链接两个链表
#自己的版本
def extend_link(s,t):
    assert is_link(s) and is_link(t)
    if(rest(s) ==empty ):
        return link(first(s),t)
    return link(first(s),extend_link(rest(s),t))

#课本中的版本：
# def extend_link(s, t):
#     assert is_link(s) and is_link(t)
#     if s == empty:
#         return t
#     else:
#         return link(first(s), extend_link(rest(s), t))


#对链表的每个元素都使用函数f，返回每个元素都使用过函数f改变过后的新的链表
def apply_to_all_link(f,s):
    if(s==empty):
        return empty
    return link(f(first(s)),apply_to_all_link(f,rest(s)))

#对链表中的每个元素都使用函数f，返回f(e)==True所对应的所有元素所组成的列表
def keep_if_link(f, s):
    if(s ==empty):
        return empty
    if(f(first(s))==True):
        return link(first(s),keep_if_link(f,rest(s)))
    else:
        return keep_if_link(f,rest(s))

four = link(1, link(2, link(3, link(4, empty))))

#返回以"，"为分隔符的字符串，其中的每个元素是链表中的每个元素
def join_link(s, separator):
    if(rest(s)==empty):
        return str(first(s))
    return str(first(s))+separator+join_link(rest(s),separator)

print(join_link(four, ", "))

