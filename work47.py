def combine(x, y):   # A function for concatenating 2 lists
	if not x and y:
		return y
	if not y and x:
		return x
	if not x and not y:
		return 'Both lists are empty'
	else:
		return x + y

a = []
b = []

combine(a, b)

temp = combine(a, b)
print temp