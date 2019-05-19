def find_last_element(x): # A function for finding last element from a list
	if not x:
		return ('The list is empty')
	elif x.count(x) == 1:
		return x[0]
	else:
		return x.pop()









