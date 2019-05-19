def find_integer(array, x):   # A simple function for finding any position on which any integer 'x' is located in anny array 'a'
	if x in array:
		i =  array.index(x)
		print i
	else:
		print ('That integer is not in the array')


def binary_search(array, l, r, x):
	if r >= l:
		mid = l + (r - l) / 2  # this is the mid
		if array[mid] == x:   # check if array[mid] is equal to the searched value
			return mid
			#print mid     # above condition true, return mid
		elif array[mid] > x: # else array[mid] > searched value
			return binary_search(array, l, mid - 1, x)  # call recursively the function, with mid - 1 
			#print binary_search(array, l, mid - 1, x) 
		else:
			return binary_search(array, mid + 1, r, x)  # else above condition is false, call recursively the function with mid + 1
			#print binary_search(array, mid + 1, r, x)
	else:
		retun -1



