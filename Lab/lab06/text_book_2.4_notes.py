chinese = ['coin', 'string', 'myriad']
suits = chinese
suits.pop()      #删除最末尾元素
print(suits)
suits.remove('string') #删除指定元素
print(suits)
suits.append('cup')  #在末尾添加元素
print(suits)
suits.extend(['sword','club'])
print(suits)
suits[2] = 'spade'
print(suits)
print(suits[0:2])
suits[0:2] = ['heart','diamond']
print(suits)

nest = list(suits)
nest[0] = suits
print(nest)
print(suits)

suits.insert(2,'Joker')
print(suits)
print(nest)

nest[0].pop(2)
print(suits)

print(suits is nest[0])      #要清楚is is not 以及 ==的区别
print(suits is ['heart', 'diamond', 'spade', 'club'])
print(suits == ['heart', 'diamond', 'spade', 'club'])

from unicodedata import lookup
print([lookup('WHITE ' + s.upper() + ' SUIT') for s in suits])

# 利用list()函数或者直接利用[]里面装for循环，都可以用来创建新列表，并且不会与原列表共享结构
#
# 元组用逗号分割以创建，标准写作格式外面需要加上括号，实践中也可以不加.元组是不可变类型
a = 1,2+3
print(a)

# 空元组以及只含有一个元素的元组
()
print(())
(10,)
print((10,))

# tupple的count()方法以及index()方法
code = ("up", "up", "down", "down") + ("left", "right") * 2
len(code)
print(code[3])
print(code.count("down"))
print(code.index("left"))

# tuppe是不可变类型，但可以改变tupple中的可变元素的值
nest = (10,20,[30,40])
nest[2].pop()
print(nest)

# dictionary类型，与lsit与tupple不同，dic类型专门用于不按连续整数索引，而是按描述型叙述存储的
# 数据的抽象类型
# dic类型用{}或者dict()函数创建
numerals = {'I':1.0 , 'V':5 , 'X':10}
print(numerals['X'])
a = dict([(3,9),(4,15),(5,15)])
print(a)
print({x:x*x for x in range(3,6)})


# 字典中每个键最多只能有一个值。添加新的键值对和更改键的现有值都可以通过赋值语句实现。
numerals['I'] = 1
numerals['L'] =50
print(numerals)

print(sum(numerals.values()))

# 字典的限制：
# 字典的键不可能包含可变的数据类型，且一个键最多只能对应一个值
# 对字典来说，一个有用的函数为get()。get()函数接收的参数为需要查找的值的键以及如果没有此键所返回的默认值
print(numerals.get('A',0))
print(numerals.get('V',0))



#课本以一个输入相同参数，但同一函数却返回不同值的例子，引入了nonlocal的概念
def make_withdraw(balance):
        """Return a withdraw function that draws down balance with each call."""
        def withdraw(amount):
            nonlocal balance                 # Declare the name "balance" nonlocal
            if amount > balance:
                return 'Insufficient funds'
            balance = balance - amount       # Re-bind the existing balance name
            return balance
        return withdraw

# withdraw = make_withdraw(100)  #通过嵌套函数实现该功能，首先进行初始化，其次在里层函数声明该参数为nonlocal的
# print(withdraw(25))
# print("**********************")
# print(withdraw(25))
# print("**********************")
# print(withdraw(60))
# print("**********************")
# print(withdraw(15))

# Non-local 的优点：如果你平行的调用两次make_withdraw()函数，则两个wd互不影响
# wd = make_withdraw(20)
# wd2 = make_withdraw(7)
#
# print(wd2(6))
# print("*****************")
# print(wd(8))
# print("*****************")

#Non-local 的弱点，如果你利用=将wd和wd2之间相互绑定，则互相之间会相互影响！
# wd = make_withdraw(12)
# wd2 = wd
# print(wd2(1))
# print("*****************")
# print(wd2(1))


#implementing lists and dictionaries
#其中消息派发的方式采用if匹配条件语句
def dictionary():
    """Return a functional implementation of a dictionary."""
    records = []

    def getitem(key):
        matches = [r for r in records if r[0] == key]
        if len(matches) == 1:
            key, value = matches[0]
            return value

    def setitem(key, value):
        nonlocal records
        non_matches = [r for r in records if r[0] != key]
        records = non_matches + [[key, value]]

    def dispatch(message, key=None, value=None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            setitem(key, value)
        elif message == 'read':
            read()

    def read():
        for i in records:
            print(i)

    return dispatch

# d = dictionary()
# d('setitem', 3, 9)
# d('setitem', 4, 16)
# print(d('getitem', 3))
# print(d('getitem', 4))
# d('read')


#另一种消息派发模式为使用dic类型进行实现，利用这种方式可以避免函数中的nonlocal声明
def account(initial_balance):
    def deposit(amount):
        dispatch['balance'] += amount
        return dispatch['balance']
    def withdraw(amount):
        if amount > dispatch['balance']:
            return 'Insufficient funds'
        dispatch['balance'] -= amount
        return dispatch['balance']
    dispatch = {'deposit':   deposit,
                'withdraw':  withdraw,
                'balance':   initial_balance}
    return dispatch

def withdraw(account, amount):
    return account['withdraw'](amount)
def deposit(account, amount):
    return account['deposit'](amount)
def check_balance(account):
    return account['balance']

# a = account(20)
# print(deposit(a, 5))
# print(withdraw(a, 17))
# print(check_balance(a))













