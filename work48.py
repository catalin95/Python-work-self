class Stack:

	def __init__(self):
		self.stack = []

	def add(self, element):
		if element not in self.stack:
			self.stack.append(element)
			return True
		else:
			print ('The item is already in the stack')

	def remove(self):
		if not self.stack:
			print ('The stack is empty')
		else:
			return self.stack.remove(self.stack[-1])

	def print_last_element(self):
		if not self.stack:
			print ('The stack is empty')
		else:
			print (self.stack[-1])
			return True

	def print_stack(self):
		if not self.stack:
			print ('The stack is empty')
		else:
			print (self.stack)
			return True

	def chek_item(self, item):
		if not self.stack:
			print ('The stack is empty')
		else:
			print ('The item is in the stack')
			return item




AStack = Stack()
AStack.add(1)
AStack.add(2)
AStack.add(3)
AStack.add(4)

AStack.print_stack()
AStack.print_last_element()
AStack.remove()
AStack.print_last_element()
AStack.print_stack()
AStack.remove()
AStack.print_last_element()
AStack.print_stack()
AStack.chek_item(10)

