def insert_items(lst, entry, elem):
	list = [i for i in range(len(lst)) if (lst[i] == entry)]
	times = 0
	for i in list:
		times +=1
		lst.insert(i+times, elem)
	return lst




large_lst2 = [1,4,4,8]
new_lst = insert_items(large_lst2, 4, 6)
print(new_lst)
new_lst = insert_items(large_lst2,4,6)
print(new_lst)