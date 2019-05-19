a = [1, 2, 3, 4, 5, 20, 46]

def find_last_element(x): # A function for finding last element from a list
	if not x:
		return ('The list is empty')
	elif x.count(x) == 1:
		return x[0]
	else:
		return x.pop()


b = []
c = find_last_element(a)
print c

find_last_element(b)
print find_last_element(b)







