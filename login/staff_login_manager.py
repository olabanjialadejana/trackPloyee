import json
from tkinter import messagebox


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
					messagebox.showinfo(title="Success", message="Welcome to Work!!")


	# except FileNotFoundError:
	# 	pass
