import json
from tkinter import messagebox
import datetime


class RegistrationError(Exception):
	pass


# def process_login_details(username, password):
# 	# Here you can add the code to process the username and password
# 	answer = [username, password]
# 	print(answer)


def process_login_details(input_username, input_password):
	json_file_path = "../database/data.json"
	with open(json_file_path, 'r') as json_file:
		data = json.load(json_file)
		for record in data.items():
			new_records = list(record)
			if input_username in new_records[0]:
				staff_password = new_records[1]['password']
				if input_password == staff_password:
					now = datetime.datetime.now()
					current_time = now.strftime('%I:%M %p')
					messagebox.showinfo(title="Login successful!!",
										message=f"Login time: {current_time}\nWelcome to Work!!!!")

					file_path = "../database/staff_attendance_record.json"

					try:
						with open(file_path, 'r') as file:
							existing_data = json.load(file)
					except FileNotFoundError:
						existing_data = []
					# Create login record
					record = {}

					staff_number = input_username
					login_time = datetime.datetime.now()
					record["Staff Number"] = staff_number
					record["Login Time"] = login_time

					existing_data.append(record)

					print(record)

					with open(file_path, 'w') as file:
						json.dump(existing_data, file, default=str, indent=4)

				else:
					messagebox.showerror(title="Login Error!!!", message="Wrong Password!!!")
				break
		else:
			messagebox.showerror(title="Username Error!!!", message="Username not found!!!")




	# except FileNotFoundError:
	# 	pass
