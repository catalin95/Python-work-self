class Stack:  # new class for creating stack object

	def __init__(self):
		self.stack = []

	def add(self, element):
		if element not in self.stack:
			self.stack.append(element)
			return True
		else:
			print ('The item is already in the stack')

	def remove(self):	# function to remove items
		if not self.stack:
			print ('The stack is empty')
		else:
			return self.stack.remove(self.stack[-1])

	def print_last_element(self):	# function to print last element
		if not self.stack:
			print ('The stack is empty')
		else:
			print (self.stack[-1])
			return True

	def print_stack(self):		# function to print the stack
		if not self.stack:
			print ('The stack is empty')
		else:
			print (self.stack)
			return True

	def chek_item(self, item):	# function to check a specifi item if it is in the stack
		if not self.stack:
			print ('The stack is empty')
		else:
			print ('The item is in the stack')
			return item



