import json
import datetime
from tkinter import messagebox


def process_login_details(input_username, input_password):
    json_file_path = "../database/data.json"
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
        for staff_number, record in data.items():
            if input_username == staff_number:
                staff_password = record['password']
                if input_password == staff_password:
                    now = datetime.datetime.now()
                    current_time = now.strftime('%I:%M %p')
                    # messagebox.showinfo(title="Login successful!!",
                    #                     message=f"Login time: {current_time}\nWelcome to Work!!!!")

                    file_path = "../database/staff_attendance_record.json"

                    try:
                        with open(file_path, 'r') as file:
                            try:
                                existing_data = json.load(file)
                            except json.JSONDecodeError:
                                existing_data = {}
                    except FileNotFoundError:
                        existing_data = {}

                    # Check if there's an existing record for the user today
                    user_record = existing_data.get(input_username, None)
                    if user_record is None or user_record.get("Login Date") != now.date().isoformat():
                        # If no record or record not for today, create a new one
                        user_record = {
                            "Login Date": now.date().isoformat(),
                            "Login Time": now.strftime('%H:%M:%S'),  # Include seconds without microseconds
                        }
                        existing_data[input_username] = user_record
                        messagebox.showinfo(title="Login successful!!",
                                            message=f"Login time: {user_record['Login Time']}\nWelcome to Work!!!!")
                    else:
                        # If a record already exists, update the "Logout Time" and calculate the "Duration"
                        user_record["Logout Time"] = now.strftime('%H:%M:%S')
                        login_time = datetime.datetime.strptime(user_record["Login Time"], '%H:%M:%S')
                        logout_time = datetime.datetime.strptime(user_record["Logout Time"], '%H:%M:%S')
                        logout_time_output = logout_time.strftime('%H:%M:%S')
                        time_difference = logout_time - login_time
                        duration_in_seconds = time_difference.total_seconds()

                        # Convert duration to hours
                        duration_in_hours = round(duration_in_seconds / 3600.0, 2)
                        user_record["Duration"] = duration_in_hours
                        messagebox.showinfo(title="Logout successful!!",
                                            message=f"Logout time: {logout_time_output}\nHave a nice day!!!!")

                    with open(file_path, 'w') as file:
                        json.dump(existing_data, file, default=str, indent=4)

                else:
                    messagebox.showerror(title="Login Error!!!", message="Wrong Password!!!")
                break
        else:
            messagebox.showerror(title="Username Error!!!", message="Username not found!!!")
