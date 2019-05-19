class Queve:

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

Aqueve = Queve()

Aqueve.add(1)
Aqueve.add(10)
Aqueve.add(20)
Aqueve.print_queve()
Aqueve.print_first_item()
Aqueve.remove()
Aqueve.print_first_item()
Aqueve.print_queve()