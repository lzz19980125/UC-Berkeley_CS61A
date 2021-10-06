#iterators是python内置的迭代器，存在针对这种数据结构的常用的两种函数，为iter()以及next()
#iter为constructor，而next()函数则作为selector
primes = [2, 3, 5, 7]
print(type(primes))
iterator = iter(primes)
print(type(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))      当对iter利用next()进行函数读取超过其本身的范围时，python会抛出异常

#当用“=”绑定两个iter时，两个iter享有相同的位置
r = range(3, 13)
s = iter(r)  # 1st iterator over r
print(next(s))
print(next(s))
print("*********")
t = iter(r)
print(next(t))
print(next(t))
print("*********")
u = t
print(next(u))
print(next(u))
print("*********")
print(next(s))
print("*********")
print(next(t))

#类似元组，列表，以及字典等数据结构都可以生成iter()
#特别是字典，其keys以及values都可以生成iter
d = {'one': 1, 'two': 2, 'three': 3}
k = iter(d)
print(next(k))
print(next(k))
print("**********")
v = iter(d.values())
print(next(v))
print(next(v))

# d.pop('one')
# print(next(k))
#iter在运行期间，不能够对数据结构进行结构更改（如添加或者删除等等），如果更改会iter会进行报错

#有一些内建的函数return iterable，譬如下面现实的map()
def double_and_print(x):
        print('***', x, '=>', 2*x, '***')
        return 2*x

s = range(3, 8)
doubled = map(double_and_print, s)
print(next(doubled))
print(next(doubled))
print("***********")
print(list(doubled))

#除此之外，filter(),zip(),reversed()函数都遵从惰性计算

#for语句的本质：在python中，序列可以通过其__iter__返回迭代器，并且该迭代器拥有__next__()方法。
#以下可以用while+异常处理去模拟for语句的实质：
counts = [1,2,3]
i = counts.__iter__()
try:
        while True:
                item = i.__next__()
                print(item)
except StopIteration:
        pass
print()

#以上语句等价于：
for item in counts:
        print(item)

#generators以及yeild声明：
#在generator函数中，利用yeild声明返回iterable
def letters_generator(start='a',end='d'):
    current = start
    while current <=end:
        yield current
        current = chr(ord(current)+1)
for letter in letters_generator():
    print(letter)

letters = letters_generator()
print(type(letters))
print(letters.__next__())
print(letters.__next__())
print(letters.__next__())
print(letters.__next__())
print("****************")

class Letters:
    def __init__(self,start = 'a',end = 'e'):
        self.start = start
        self.end = end
    def __iter__(self):
        return letters_generator(self.start,self.end)

b_to_k = Letters('b','k')
first_iterator = b_to_k.__iter__()
print(next(first_iterator))
print(next(first_iterator))

second_iterator = iter(b_to_k)
print(second_iterator.__next__())
print(first_iterator.__next__())
print(first_iterator.__next__())
print(second_iterator.__next__())
print(second_iterator.__next__())
print("************************")












