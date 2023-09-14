from tkinter import *
from tkinter import ttk  # Import ttk for the Treeview widget
from welcome_page_UI import WelcomePageUI


class ManagerDashboard_UI:
	def __init__(self):
		self.window = Tk()
		self.window.title("Admin Dashboard")
		self.window.geometry("900x600")
		self.window.config(background="#27374D")

		self.canvas = Canvas(width=900, height=100, background="#DDE6ED")
		self.logo_img = PhotoImage(file="logo.png")
		self.canvas.create_image(450, 50, image=self.logo_img)
		self.canvas.grid(column=0, row=0)

		self.go_back_img = PhotoImage(file="samples/welcome-page-logos/icons8-go-back-48.png")
		self.go_back_button = Button(width=48, height=48, text='go_back',
									 image=self.go_back_img, command=self.go_back_to_welcome_page)
		# Position the button at the upper left part of the canvas
		self.canvas.create_window(10, 10, anchor="nw", window=self.go_back_button)

		self.canvas2 = Canvas(width=900, height=500, background="#526D82")
		self.canvas2.create_rectangle(10, 490, 890, 10, fill="#9DB2BF")
		self.canvas2.grid(column=0, row=1)

		# Create a custom style for column headers
		bold_font = ('TkDefaultFont', 10, 'bold')  # Change the font size and style as needed
		style = ttk.Style()
		style.configure("Bold.Treeview.Heading", font=bold_font)

		# Create the table (treeview)
		self.table = ttk.Treeview(columns=('staff_number', 'first_name', 'last_name', 'age', 'telephone', 'email', 'department_unit', 'position', 'pay'), show='headings', style="Bold.Treeview")
		self.table.heading('staff_number', text='Staff Number')
		self.table.heading('first_name', text='First Name')
		self.table.heading('last_name', text='Last Name')
		self.table.heading('age', text='Age')
		self.table.heading('telephone', text='Telephone')
		self.table.heading('email', text='Email')
		self.table.heading('department_unit', text='Department/Unit')
		self.table.heading('position', text='Position')
		self.table.heading('pay', text='Pay')

		# Define the column widths to fit within the rectangle
		self.table.column('staff_number', width=105)
		self.table.column('first_name', width=110)
		self.table.column('last_name', width=100)
		self.table.column('age', width=40)
		self.table.column('telephone', width=100)
		self.table.column('email', width=150)
		self.table.column('department_unit', width=120)
		self.table.column('position', width=70)
		self.table.column('pay', width=80)

		self.canvas2.create_window(12, 60, anchor="nw", window=self.table)  # Adjust the coordinates as needed

		self.window.mainloop()

	def go_back_to_welcome_page(self):
		self.window.destroy()
		WelcomePageUI()


dashboard = ManagerDashboard_UI()
