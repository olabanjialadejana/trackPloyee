from tkinter import *
from tkinter import ttk
import random


window = Tk()
window.geometry('1200x500')
window.title('Admin Dashboard')

# data
first_name = ['Chris', 'Beckham', 'Peckham', 'Ferguson', 'Mourinho', 'Tracker', 'Lion', 'Chicke', 'Tall', 'Test', 'Naughting']
last_name = ['Smith', 'Brown', 'Charlie', 'James', 'Hawkins', 'Kemi', 'Teni', 'Tunde', 'Cole', 'Violet']
status = ['In', 'In', 'Out']
date = ['Today', 'Today', 'Today', 'Yesterday']
time = ['8:05AM', '4:15PM', '10:05PM']


# treeview
table = ttk.Treeview(columns=('first_name', 'last_name', 'status', 'date', 'time'), show='headings')
table.heading('first_name', text='First Name')
table.heading('last_name', text='Last Name')
table.heading('status', text='Status')
table.heading('date', text='Date')
table.heading('time', text='Time')
table.pack(fill='both', expand=True)

# insert values into the table
# table.insert(parent='', index=0, values=('John', 'Doe', 'In', 'Today', '14:54'))
for index in range(100):
	table.insert(parent='', index=index, values=(random.choice(first_name),
												 random.choice(last_name),
												 random.choice(status),
												 random.choice(date),
												 random.choice(time)))



window.mainloop()