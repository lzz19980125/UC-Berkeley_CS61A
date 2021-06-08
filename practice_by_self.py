def if_function(condition, true_result, false_result):
    if condition:
        return true_result
    else:
        return false_result


def if_function1(condition,true_result,false_result):
	if condition():
		return true_result()
	else:
		return false_result()

def with_if_statement():
    if cond():
        return true_func()
    else:
        return false_func()

def with_if_function():
    return if_function(cond(), true_func(), false_func())

def with_if_function1():
	return if_function1(cond,true_func,false_func)

def cond():
    return  False

def true_func():
    print(42)

def false_func():
    print(47)


# result = with_if_function()
# print(result)
#
# result = with_if_statement()
# print(result)

result = with_if_function1()
print(result)