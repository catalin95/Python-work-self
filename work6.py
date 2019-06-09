class Node:	# Class for creating linked lists
	def __init__(self, element):	
		self.element = element 
		self.next = None	# This initially point to nothing

	

	def print_list(self):		# Method for printing the list
		if not self:
			print ('The list is empty')
		else:
			while self:
				print (self.element)	
				self = self.next	# Here is sets self to reference self.next and the loop continues if self is not empty
	

	def get_next_item(self):		# Method for getting the next item item from the list
		if not self:
			print ('The linked list is empty')
		else:
			self = self.next 	# You need to set self to reference self.next instance variable
			print self.element	# Then you print the instance variable for self, because self.element is set set to elemnt

	def print_remaim(self):		# Method for printing the first and remaining item of the linked list
		if not self:
			print ('The list is empty')
		else:
			#a = list(print_list(self))
			a = list()		# Creates a new empty list a
			while self:		# Inserts all elements from the linked list into the emtpy list a
				a.append(self.element)
				self = self.next
			print (a[0])	# Prints the first element from the list
			a.remove(a[0])	# Removes the first element from the list
			print (a)

	def remove(self, item):		# Method for removing an item from the list
		if not self:
			print ('The list is empty')
		else:
			a = list()		# Creates a new empty list a
			while self:		# Inserts all elemnts from the linked list into the empty list a
				a.append(self.element)	
				self = self.next
			i = a.index(item)	# Finds the index for the searched element 
			a.remove(a[i])		# Removes the searched element
			print (a)
			return True


