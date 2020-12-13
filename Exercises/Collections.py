#! Python3

# Class for creating a stack structure, implemented using list
class Stack(object):  

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


# Class for creating queve structure, implemeted using list
class Queve(object):	

	def __init__(self):
		self.queve = []

	def add(self, item):	
		return self.queve.append(item)

	def remove(self):
		if not self.queve:
			print ('The queve is empty')
		else:
			return self.queve.remove(self.queve[0])

	def print_first_item(self):	
		if not self.queve:
			print ('The queve is empty')
		else:
			print (self.queve[0])
			return True

	def print_queve(self):
		if not self.queve:
			print ('The queve is empty')
		else:
			print (self.queve)
			return True


# class for creating a linked list, you should initialize the object with a list to work
class Node(object):

	def __init__(self, element):	
		self.element = element 
		self.next = None

	def print_list(self):
		if not self:
			print ('The list is empty')
		else:
			while self:
				print (self.element)	
				self = self.next
	
	def get_next_item(self):
		if not self:
			print ('The linked list is empty')
		else:
			self = self.next 
			print self.element

	def print_remaim(self):
		if not self:
			print ('The list is empty')
		else:
			a = list()
			while self:
				a.append(self.element)
				self = self.next
			print (a[0])
			a.remove(a[0])
			print (a)

	def remove(self, item):
		if not self:
			print ('The list is empty')
		else:
			a = list()
			while self:
				a.append(self.element)	
				self = self.next
			i = a.index(item)
			a.remove(a[i])
			print (a)
			return True

