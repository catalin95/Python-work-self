#! Python3
# Function for conbining 2 lists

def combine(x, y): 
	if not x and y:
		return y
	if not y and x:
		return x
	if not x and not y:
		return 'Both lists are empty'
	else:
		return x + y
