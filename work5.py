class Queve:	# class for creating queve objects

	def __init__(self):
		self.queve = []

	def add(self, item):	# function to add a new item to the stak
		return self.queve.append(item)

	def remove(self):	# function to remove an item from stack
		if not self.queve:
			print ('The queve is empty')
		else:
			return self.queve.remove(self.queve[0])

	def print_first_item(self):	# function to print the first item from a stack
		if not self.queve:
			print ('The queve is empty')
		else:
			print (self.queve[0])
			return True

	def print_queve(self):		# function to print the queve
		if not self.queve:
			print ('The queve is empty')
		else:
			print (self.queve)
			return True

