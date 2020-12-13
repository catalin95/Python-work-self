#! Python3
# functions for finding elements in some collections

def find_integer(array, x):   
	if x in array:
		i =  array.index(x)
		print(i)
	else:
		print('That integer is not in the array')


def binary_search(array, l, r, x):	 
	if r >= l:
		mid = l + (r - l) / 2 
		if array[mid] == x:   
			return mid
		elif array[mid] > x: 
			return binary_search(array, l, mid - 1, x) 
		else:
			return binary_search(array, mid + 1, r, x)
	else:
		return -1

# A function for finding last element from a list
def find_last_element(x): 
	if not x:
		return ('The list is empty')
	elif len(x) == 1:
		return x[0]
	else:
		return x.pop()



