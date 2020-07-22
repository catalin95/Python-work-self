#! python3

from tkinter import *
from pyodbc import *
#import pyodbc

root = Tk()
root.title('SQL Simulator')
root.geometry("400x400")

connection_keeper = 0

def connection():
	try:
		con = pyodbc.connect('Driver={SQL Server};'
                      'Server=TIMNTE735;'
                      'Database=TIM_FF2819_ENEL_T;'
                      'Trusted_Connection=yes;')
					  
		global connection_keeper 
		connection_keeper = con.cursor()
					  
		a = Label(root, text = "Connection to database extablished!", fg = 'green')
		a.pack()
		
		#connection_keeper.close()
		return True
	except:
		a = Label(root, text = "Can't connect to database!", fg = 'red')
		a.pack()


connection()
		
e = Entry(root, width = 50)
e.pack()

def sql_command(command = e.get()):
	try:
		connection_keeper.execute(str(command))
		a = Label(root, text = command)
		a.pack()
	except:
		a = Label(root, text = "Not a valid SQL command entered!")
		a.pack()

def click():
	a = Label(root, text = sql_command())
	a.pack()
	
def check():
	if connection_keeper == 0:
		myButton1 = Button(root, text = 'Click to execute SQL command', state = 'disable', command = click, fg = 'red')
		myButton1.pack()
	else:
		myButton1 = Button(root, text = 'Click to execute SQL command', state = 'active', command = click, fg = 'blue')
		myButton1.pack()
	
def close_connection():
	if isinstance(connection_keeper, int):
		pass
	else:
		connection_keeper.close()
	
#label = Label(root, text = connection())
#label.pack()

check()
close_connection()

		
	
#myButton1 = Button(root, text = 'Click to execute SQL command', command = Click, fg = 'blue')

#myButton1.pack()

root.mainloop()


