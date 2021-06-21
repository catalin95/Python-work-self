#! Python3
# Function for conbining 2 lists

class Operations(object):

	def __init__(self, x):
		self.x = x


	def combine(self, other):
		if not self.x and not other.x:
			return other.x
		elif not other.x and self.x:
			return self.x
		elif not self.x and not other.x:
			return "Both lists are empty"
		else:
			new_object = Operations(self.x + other.x)


'''
def combine(x, y):
	if not x and y:
		return y
	if not y and x:
		return x
	if not x and not y:
		return 'Both lists are empty'
	else:
		return x + y
'''
