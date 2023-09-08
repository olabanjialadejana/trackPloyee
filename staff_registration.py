from tkinter import *

FONT_NAME = "Cambria"


class StaffRegistrationUI:
	def __init__(self):
		self.window = Tk()
		self.window.title("TrackPloyee")
		self.window.geometry("900x600")
		self.window.config(background="#27374D")
		self.canvas = Canvas(width=900, height=150, background="#DDE6ED")
		self.logo_img = PhotoImage(file="logo.png")
		self.canvas.create_image(450, 70, image=self.logo_img)
		self.canvas.grid(column=0, row=0)
		self.canvas2 = Canvas(width=900, height=450, background="#526D82")
		self.canvas2.create_rectangle(180, 430, 720, 20, fill="#9DB2BF")
		self.canvas2.grid(column=0, row=1)



		## Labels
		self.theme = Label(text="New Staff Registration", font=(FONT_NAME, 15), background="#9DB2BF")
		self.canvas2.create_window(450, 45, window=self.theme)

		# Firstname
		self.first_name = Label(text="First Name:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(300, 70, window=self.first_name)
		self.first_name_entry = Entry(width=32, fg='grey')
		self.first_name_entry.insert(0, "First Name")
		self.canvas2.create_window(450, 70, window=self.first_name_entry)


		# Lastname
		self.next_kin_telephone = Label(text="Last Name:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(300, 100, window=self.next_kin_telephone)
		self.last_name_entry = Entry(width=32, fg='grey')
		self.last_name_entry.insert(0, "Last Name")
		self.canvas2.create_window(450, 100, window=self.last_name_entry)

		# Age
		self.age_label = Label(text="Age:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(300, 120, window=self.age_label)
		# Use Spinbox to create a scrolling number input field
		self.age_spinbox = Spinbox(self.canvas2, from_=18, to=60, width=5)
		self.canvas2.create_window(450, 120, window=self.age_spinbox)

		# Telephone
		self.next_kin_telephone = Label(text="Telephone:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(300, 140, window=self.next_kin_telephone)
		self.next_kin_telephone_entry = Entry(width=32, fg='grey')
		self.next_kin_telephone_entry.insert(0, "Telephone")
		self.canvas2.create_window(450, 140, window=self.next_kin_telephone_entry)

		# Email
		self.email = Label(text="Email:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(300, 160, window=self.email)
		self.email_entry = Entry(width=32, fg='grey')
		self.email_entry.insert(0, "Email")
		self.canvas2.create_window(450, 160, window=self.email_entry)

		# Address
		self.position = Label(text="Address:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(300, 180, window=self.position)
		self.position = Entry(width=32, fg='grey')
		self.position.insert(0, "Address")
		self.canvas2.create_window(450, 180, window=self.position)

		# Next of kin section
		self.official = Label(text="Next of kin details", font=(FONT_NAME, 12), background="#9DB2BF")
		self.canvas2.create_window(450, 210, window=self.official)

		self.department = Label(text="First Name:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(300, 210, window=self.department)
		self.department = Entry(width=32, fg='grey')
		self.department.insert(0, "next of kin first name")
		self.canvas2.create_window(450, 210, window=self.department)

		self.position = Label(text="Address:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(300, 250, window=self.position)
		self.position = Entry(width=32, fg='grey')
		self.position.insert(0, "Address")
		self.canvas2.create_window(450, 250, window=self.position)

		self.next_kin_telephone = Label(text="Telephone:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(300, 270, window=self.next_kin_telephone)
		self.next_kin_telephone_entry = Entry(width=32, fg='grey')
		self.next_kin_telephone_entry.insert(0, "Telephone")
		self.canvas2.create_window(450, 270, window=self.next_kin_telephone_entry)

		# official section
		self.official = Label(text="Work details", font=(FONT_NAME, 12), background="#9DB2BF")
		self.canvas2.create_window(450, 300, window=self.official)

		self.department = Label(text="Department:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(300, 320, window=self.department)
		self.department_entry = Entry(width=32, fg='grey')
		self.department_entry.insert(0, "Department")
		self.canvas2.create_window(450, 320, window=self.department_entry)

		self.position = Label(text="Position:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(300, 340, window=self.position)
		self.position_entry = Entry(width=32, fg='grey')
		self.position_entry.insert(0, "Position")
		self.canvas2.create_window(450, 340, window=self.position_entry)

		self.pay = Label(text="Pay:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(300, 360, window=self.pay)
		self.pay_entry = Entry(width=32, fg='grey')
		self.pay_entry.insert(0, "Pay")
		self.canvas2.create_window(450, 360, window=self.pay_entry)



		self.window.mainloop()


test = StaffRegistrationUI()
