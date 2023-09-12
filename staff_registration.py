from tkinter import *
from tkinter import messagebox
from datetime import datetime
import json
import os
print("Current directory:", os.getcwd())

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
		self.go_back_img = PhotoImage(file="samples/welcome-page-logos/icons8-go-back-48.png")
		self.go_back_button = Button(width=48, height=48, text='go_back',
									 image=self.go_back_img, command=self.go_back_to_welcome_page)
		# Position the button at the upper left part of the canvas
		self.canvas.create_window(10, 10, anchor="nw", window=self.go_back_button)
		self.canvas2 = Canvas(width=900, height=450, background="#526D82")
		self.canvas2.create_rectangle(180, 430, 720, 20, fill="#9DB2BF")
		self.canvas2.grid(column=0, row=1)

		# Labels
		self.theme = Label(text="New Staff Registration", font=(FONT_NAME, 15), background="#9DB2BF")
		self.canvas2.create_window(450, 45, window=self.theme)

		# Firstname
		self.first_name = Label(text="First Name:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(315, 70, window=self.first_name)
		self.first_name_entry = Entry(width=32, fg='grey')
		self.first_name_entry.focus()
		self.canvas2.create_window(450, 70, window=self.first_name_entry)

		# Lastname
		self.next_kin_telephone = Label(text="Last Name:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(315, 95, window=self.next_kin_telephone)
		self.last_name_entry = Entry(width=32, fg='grey')
		self.last_name_entry.focus()
		self.canvas2.create_window(450, 95, window=self.last_name_entry)

		# Age
		self.age_label = Label(text="Age:", font=(FONT_NAME, 10), background="#9DB2BF", justify="right")
		self.canvas2.create_window(334, 120, window=self.age_label)
		# Use Spinbox to create a scrolling number input field
		self.age_spinbox = Spinbox(self.canvas2, from_=18, to=60, width=5, justify="left")
		self.canvas2.create_window(374, 120, window=self.age_spinbox)

		# Telephone
		self.telephone = Label(text="Telephone:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(315, 145, window=self.telephone)
		self.telephone_entry = Entry(width=32, fg='grey')
		self.telephone_entry.focus()
		self.canvas2.create_window(450, 145, window=self.telephone_entry)

		# Email
		self.email = Label(text="Email:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(327, 170, window=self.email)
		self.email_entry = Entry(width=32, fg='grey')
		self.email_entry.focus()
		self.canvas2.create_window(450, 170, window=self.email_entry)

		# Address
		self.address = Label(text="Address:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(322, 195, window=self.address)
		self.address_entry = Entry(width=32, fg='grey')
		self.address_entry.focus()
		self.canvas2.create_window(450, 195, window=self.address_entry)

		# Next of kin section
		self.next_kin = Label(text="Next of kin details", font=(FONT_NAME, 12), background="#9DB2BF")
		self.canvas2.create_window(450, 220, window=self.next_kin)

		self.next_kin_name = Label(text="Name:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(315, 245, window=self.next_kin_name)
		self.next_kin_name_entry = Entry(width=32, fg='grey')
		self.next_kin_name_entry.focus()
		self.canvas2.create_window(450, 245, window=self.next_kin_name_entry)

		self.next_kin_name_address = Label(text="Address:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(322, 270, window=self.next_kin_name_address)
		self.next_kin_name_address_entry = Entry(width=32, fg='grey')
		self.next_kin_name_address_entry.focus()
		self.canvas2.create_window(450, 270, window=self.next_kin_name_address_entry)

		self.next_kin_telephone = Label(text="Telephone:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(315, 295, window=self.next_kin_telephone)
		self.next_kin_telephone_entry = Entry(width=32, fg='grey')
		self.next_kin_telephone_entry.focus()
		self.canvas2.create_window(450, 295, window=self.next_kin_telephone_entry)

		# official section
		self.official = Label(text="Work details", font=(FONT_NAME, 12), background="#9DB2BF")
		self.canvas2.create_window(450, 320, window=self.official)

		self.department = Label(text="Department:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(314, 345, window=self.department)
		self.department_entry = Entry(width=32, fg='grey')
		self.department_entry.focus()
		self.canvas2.create_window(450, 345, window=self.department_entry)

		self.position = Label(text="Position:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(320, 370, window=self.position)
		self.position_entry = Entry(width=32, fg='grey')
		self.position_entry.focus()
		self.canvas2.create_window(450, 370, window=self.position_entry)

		self.pay = Label(text="Pay:", font=(FONT_NAME, 10), background="#9DB2BF")
		self.canvas2.create_window(333, 395, window=self.pay)
		self.pay_entry = Entry(width=32, fg='grey')
		self.pay_entry.focus()
		self.canvas2.create_window(450, 395, window=self.pay_entry)

		self.submit_img = PhotoImage(file="samples/welcome-page-logos/icons8-upload-64.png")
		self.submit_button = Button(width=70, height=68, text='submit',
									image=self.submit_img,
									command=lambda: self.save_registration_data())
		# self.staff_data = self.get_all_entry_values()
		# Position the button at the upper left part of the canvas
		self.canvas2.create_window(670, 405, anchor="se", window=self.submit_button)

		self.window.mainloop()

	def get_all_entry_values(self):
		first_name = self.first_name_entry.get()
		last_name = self.last_name_entry.get()
		age = self.age_spinbox.get()
		telephone = self.telephone_entry.get()
		email = self.email_entry.get()
		address = self.address_entry.get()
		next_kin_name = self.next_kin_name_entry.get()
		next_kin_address = self.next_kin_name_address_entry.get()
		next_kin_telephone = self.next_kin_telephone_entry.get()
		department = self.department_entry.get()
		position = self.position_entry.get()
		pay = self.pay_entry.get()

		if '' not in (first_name, last_name, age, telephone, email, address, next_kin_name, next_kin_address,
					  next_kin_telephone, department, position, pay):
			# automatically generate unique staff number
			year = datetime.now().strftime('%Y')
			staff_number = year + "00" + str(1)
			registration_data = {
				staff_number: {
					'first name': first_name,
					'last name': last_name,
					'age': age,
					'telephone': telephone,
					'email': email,
					'address': address,
					'next of kin': next_kin_name,
					'next of kin address': next_kin_address,
					'next of kin telephone': next_kin_telephone,
					'department/unit': department,
					'position': position,
					'pay': pay
				},
				# Add more data here if needed
			}
			return registration_data
		else:
			return None

	def save_registration_data(self):
		new_data = self.get_all_entry_values()
		try:
			with open("data.json", "r+") as data_file:
				# Read old data
				data = json.load(data_file)
		except (FileNotFoundError, json.JSONDecodeError):
			data = []

		# create a new but sequenced staff number
		# get last key
		last_key = list(new_data.keys())[-1]
		# extract the last character in the key
		last_character = int(last_key[-1])
		year = datetime.now().strftime('%Y')
		staff_number = year + "00" + str(last_character + 1)
		new_data[staff_number] = new_data.pop(last_key)

		data.append(new_data)

		with open('data.json', 'w') as data_file:
			json.dump(data, data_file, indent=4)

		messagebox.showinfo(title="Registration successful!!", message="New staff registration successful")
		self.window.destroy()
		from welcome_page_UI import WelcomePageUI
		WelcomePageUI()

	def go_back_to_welcome_page(self):
		self.window.destroy()
		from welcome_page_UI import WelcomePageUI
		WelcomePageUI()
