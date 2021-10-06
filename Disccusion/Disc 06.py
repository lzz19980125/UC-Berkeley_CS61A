#Questions 1.1 solution
def memory(n):
    def f(g):
        nonlocal n
        n = g(n)
        return n
    return f

f = memory(10)
print(f(lambda  x:x*2))
print("**************")
print(f(lambda  x:x-7))
print("**************")
print(f(lambda  x:x>5))


#Questions 2.3 solution
def group_by(s,fn):
    grouped = {}
    for i in s:
        key = fn(i)
        if(key in grouped):
            grouped[key].append(i)
        else:
            grouped[key] = [i]
    return grouped

print(group_by([12,23,14,45],lambda p:p //10))
print("**************")
print(group_by(range(-3,4),lambda x: x*x))


#Question 2.4 solution
def add_this_many(x,el,s):
    times = 0
    for i in s:
        if(i==x):
            times +=1
    for i in range(times):
        s.append(el)
    return s


s = [1, 2, 4, 2, 1]
print(add_this_many(1,5,s))
print("******************")
print(add_this_many(2,2,s))

#Question 3.1 solution:
s = [[1, 2]]
i = iter(s)
j = iter(next(i))
print(next(j))
s.append(3)
print(next(i))
print(next(j))

#Question 4.1 solution:
def filter(iterable,fn):
    for i in iterable:
        if(fn(i)==True):
            yield  i
is_even = lambda x:x%2 ==0
print(list(filter(range(5),is_even)))
print("*****************************")
all_odd = (2 * y - 1 for y in range(5))
print(list(filter(all_odd,is_even)))
print("*****************************")
naturals = (n for n in range(1, 100))
s = filter(naturals,is_even)
print(next(s))
print(next(s))
print("*****************************")


#Question 4.2 solutions:
def merge(a, b):
    A, B = next(a), next(b)
    while True:
        if(A>B):
            yield B
            B = next(b)
        if(A==B):
            yield B
            A = next(a)
            B=next(b)
        if(A<B):
            yield A
            A = next(a)


def sequence(start,step):
    while True:
        yield start
        start += step

a = sequence(2,3)
b = sequence(3,2)
result = merge(a,b)
print([next(result) for _ in range(10)])
