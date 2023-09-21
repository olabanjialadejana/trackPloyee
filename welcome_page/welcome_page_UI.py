from tkinter import *
import datetime
import os

# Get the absolute path to the directory containing this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate to the image directory from the script's location
image_dir = os.path.join(script_dir, "..", "images")

os.chdir(image_dir)


class WelcomePageUI:
	def __init__(self):
		self.window = Tk()
		self.window.title("TrackPloyee")
		self.window.geometry("900x600")
		self.window.config(background="#27374D")
		self.canvas = Canvas(width=900, height=150, background="#DDE6ED")
		self.logo_img = PhotoImage(file="logo.png")
		self.canvas.create_image(450, 100, image=self.logo_img)
		self.canvas.grid(column=0, row=0)
		self.canvas2 = Canvas(width=900, height=450, background="#526D82")
		self.canvas2.create_rectangle(210, 400, 690, 50, fill="#9DB2BF")
		self.canvas2.grid(column=0, row=1)

		self.initial_time = datetime.datetime.now().strftime('%I:%M %p')
		self.initial_date = datetime.datetime.now().strftime('%A, %B %d')
		self.date_text = self.canvas2.create_text(450, 170, text=self.initial_date, font=("Arial", 10))
		self.time_text = self.canvas2.create_text(450, 130, text=self.initial_time, font=("Arial", 24))
		self.canvas2.grid(column=0, row=1)
		self.manager_img = PhotoImage(file="icons8-manager-100.png")
		self.all_staff_img = PhotoImage(file="all_staff_login.png")

		self.all_staff_login_button = Button(width=100, height=100, text='New Employee Registration',
											 image=self.all_staff_img, command=self.go_to_login_ui_options)
		self.canvas2.create_window(380, 250, window=self.all_staff_login_button)
		self.manager_login_button = Button(width=100, height=100, text='Manager Login', image=self.manager_img, command=self.go_to_manager_login)
		self.canvas2.create_window(550, 250, window=self.manager_login_button)
		self.staff_login_text = self.canvas2.create_text(380, 320, text="Staff Login", font=("Arial", 10, "bold"))
		self.manager_login_text = self.canvas2.create_text(550, 320, text="Manager Login", font=("Arial", 10, "bold"))

		self.window.mainloop()

	def update_time(self):
		now = datetime.datetime.now()
		current_date = now.strftime('%A, %B %d')
		current_time = now.strftime('%I:%M %p')
		self.canvas2.itemconfig(self.time_text, text=current_time)
		self.canvas2.itemconfig(self.date_text, text=current_date)

	def open_password_login(self):
		self.window.destroy()
		from login.login_UI import LoginUI
		LoginUI()

	def open_staff_registration(self):
		self.window.destroy()
		from staff.staff_registration_UI import StaffRegistrationUI
		StaffRegistrationUI()

	def go_to_login_ui_options(self):
		self.window.destroy()
		from login.login_UI_options import LoginUIOptions
		LoginUIOptions()

	def go_to_manager_login(self):
		self.window.destroy()
		from manager.manager_login_UI import ManagerLoginUI
		ManagerLoginUI()
