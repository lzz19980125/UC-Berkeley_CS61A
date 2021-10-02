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



