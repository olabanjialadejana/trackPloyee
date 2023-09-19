from datetime import datetime
import json
from tkinter import messagebox
from login_UI_options import LoginUIOptions


class RegistrationError(Exception):
	pass


def get_all_entry_values(self):
	first_name = self.first_name_entry.get()
	last_name = self.last_name_entry.get()
	age = self.age_spinbox.get()
	telephone = self.telephone_entry.get()
	email = self.email_entry.get()
	address = self.address_entry.get()
	password = self.password_entry.get()
	password_confirmation = self.password_confirmation_entry.get()
	next_kin_name = self.next_kin_name_entry.get()
	next_kin_address = self.next_kin_name_address_entry.get()
	next_kin_telephone = self.next_kin_telephone_entry.get()
	department = self.department_entry.get()
	position = self.position_entry.get()
	pay = self.pay_entry.get()

	try:
		if '' in (first_name, last_name, age, telephone, email, address, password, password_confirmation, next_kin_name,
				  next_kin_address,
				  next_kin_telephone, department, position, pay):
			raise RegistrationError("Empty fields are not allowed")

		if password != password_confirmation:
			raise RegistrationError("Password and password confirmation do not match.")

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
				'password': password,
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
	except RegistrationError as e:
		messagebox.showerror(title="Registration Error", message=str(e))
		return None


def save_registration_data(self):
	new_data = get_all_entry_values(self)
	try:
		with open("data.json", "r") as data_file:
			# Read old data
			data = json.load(data_file)

			# extract the last staff number from old data
			previous_staff_number = list(data.keys())[-1]
			previous_staff_number = str(previous_staff_number)

			# Generate new staff number
			new_staff_number = str(int(previous_staff_number) + 1)

			# Rename the new staff number in new_data
			new_data[new_staff_number] = new_data.pop(list(new_data.keys())[0])

			data.update(new_data)

			with open('data.json', 'w') as file:
				json.dump(data, file, indent=4)

			messagebox.showinfo(title="Registration successful!!", message="New staff registration successful")
			self.window.destroy()
			WelcomePageUI()

	except (FileNotFoundError, json.JSONDecodeError):
		data = {}

		year = datetime.now().strftime('%Y')
		staff_number = year + "00" + "1"
		data[staff_number] = new_data

		data.update(new_data)

		with open('data.json', 'w') as data_file:
			json.dump(data, data_file, indent=4)

		messagebox.showinfo(title="Registration successful!!", message="New staff registration successful")
		self.window.destroy()
		LoginUIOptions()
