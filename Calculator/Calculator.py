#! python3
from tkinter import *

root = Tk()
root.title('Calculator')

e = Entry(root, width = 40, borderwidth = 5)
e.grid(row=0, column=0, columnspan=7, padx=10, pady = 10)


def button_click(number):
	#e.delete(0, 'end')
	current = e.get()
	e.delete(0, 'end')
	e.insert(0, str(current) + str(number))

def button_clear():
	e.delete(0, 'end')
	
def button_add():
	first_number = e.get()
	global f_num
	global math
	math = 'addition'
	f_num = float(first_number)
	e.delete(0, 'end')
	
def button_equal():
	second_number = e.get()
	e.delete(0, 'end')
	
	if math == 'addition': 
		e.insert(0, f_num + int(second_number))
	elif math == 'substraction':
		e.insert(0, f_num - int(second_number))
	elif math == 'multiplication':
		e.insert(0, f_num * int(second_number))
	else:
		e.insert(0, f_num / int(second_number))
		
def button_substract():
	first_number = e.get()
	global f_num
	global math
	math = 'substraction'
	f_num = float(first_number)
	e.delete(0, 'end')
	
def button_multiply():
	first_number = e.get()
	global f_num
	global math
	math = 'multiplication'
	f_num = float(first_number)
	e.delete(0, 'end')
	
def button_divide():
	first_number = e.get()
	global f_num
	global math
	math = 'division'
	f_num = float(first_number)
	e.delete(0, 'end')
	

# Define Buttons
button1 = Button(root, text = '1', padx = 40, pady = 20, command = lambda: button_click(1), fg = 'green')
button2 = Button(root, text = '2', padx = 40, pady = 20, command = lambda: button_click(2), fg = 'green')
button3 = Button(root, text = '3', padx = 40, pady = 20, command = lambda: button_click(3), fg = 'green')
button4 = Button(root, text = '4', padx = 40, pady = 20, command = lambda: button_click(4), fg = 'green')
button5 = Button(root, text = '5', padx = 40, pady = 20, command = lambda: button_click(5), fg = 'green')
button6 = Button(root, text = '6', padx = 40, pady = 20, command = lambda: button_click(6), fg = 'green')
button7 = Button(root, text = '7', padx = 40, pady = 20, command = lambda: button_click(7), fg = 'green')
button8 = Button(root, text = '8', padx = 40, pady = 20, command = lambda: button_click(8), fg = 'green')
button9 = Button(root, text = '9', padx = 40, pady = 20, command = lambda: button_click(9), fg = 'green')
button0 = Button(root, text = '0', padx = 40, pady = 20, command = lambda: button_click(0), fg = 'green')

button_add = Button(root, text = '+', padx = 39, pady = 20, command = button_add, fg = 'blue')
button_equal = Button(root, text = '=', padx = 89, pady = 20, command = button_equal, fg = 'orange')
button_clear = Button(root, text = 'Clear', padx = 79, pady = 20, command = button_clear, fg = 'red')
button_substract = Button(root, text = '-', padx = 40, pady = 20, command = button_substract, fg = 'blue')
button_multiply = Button(root, text = '*', padx = 40, pady = 20, command = button_multiply, fg = 'blue')
button_divide = Button(root, text = '/', padx = 40, pady = 20, command = button_divide, fg = 'blue')

# Put buttons on screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button0.grid(row=4, column=0)

button_clear.grid(row=6, column=0, columnspan=2)
button_add.grid(row=4, column=1)
button_equal.grid(row=5, column=0, columnspan=2)
button_substract.grid(row=4, column=2)
button_multiply.grid(row=5, column=2)
button_divide.grid(row=6, column=2)


#myButton1 = Button(root, text = 'Click to say Hello!', command = myClick, fg = 'blue')


root.mainloop()


