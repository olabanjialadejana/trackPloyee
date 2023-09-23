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
			# print(new_records)
			if input_username in new_records[0]:
				user_record = new_records
				staff_password = new_records[1]['password']
				if input_password == staff_password:
					now = datetime.datetime.now()
					current_time = now.strftime('%I:%M %p')
					messagebox.showinfo(title="Login successful!!",
										message=f"Login time: {current_time}\nWelcome to Work!!!!")

				else:
					messagebox.showerror(title="Login Error!!!", message="Wrong Password!!!")
			elif input_username not in new_records[0]:
				messagebox.showerror(title="Username Error!!!", message="Username not found!!!")
				break



	# except FileNotFoundError:
	# 	pass
