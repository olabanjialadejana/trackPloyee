from tkinter import *


class ManagerDashboardUI:
	def __init__(self):
		self.window = Tk()
		self.window.title("TrackPloyee")
		self.window.geometry("900x600")
		self.window.config(background="#27374D")
		self.canvas = Canvas(width=900, height=150, background="#DDE6ED")
		self.logo_img = PhotoImage(file="../images/logo.png")
		self.canvas.create_image(450, 100, image=self.logo_img)
		self.canvas.grid(column=0, row=0)
		self.canvas2 = Canvas(width=900, height=450, background="#526D82")
		self.canvas2.create_rectangle(210, 400, 690, 50, fill="#9DB2BF")
		self.canvas2.grid(column=0, row=1)

		self.go_back_img = PhotoImage(file="../images/icons8-go-back-48.png")
		self.go_back_button = Button(width=48, height=48, text='go_back',
									 image=self.go_back_img, command=self.go_to_manager_login)
		# Position the go-back-button at the upper left part of the canvas
		self.canvas.create_window(10, 10, anchor="nw", window=self.go_back_button)

		self.staff_dashboard_img = PhotoImage(file="../images/icons8-dashboard-100.png")
		self.register_new_staff = PhotoImage(file="../images/icons8-new-staff-100.png")
		self.additional_tasks = PhotoImage(file="../images/icons8-more-100.png")


		self.register_new_staff_button = Button(width=100, height=100, text='New Employee Registration',
											 image=self.register_new_staff, command=self.open_staff_registration)
		self.canvas2.create_window(300, 220, window=self.register_new_staff_button)

		self.staff_dashboard_button = Button(width=100, height=100, text='Manager Login', image=self.staff_dashboard_img, command=self.go_to_staff_dashboard)
		self.canvas2.create_window(450, 220, window=self.staff_dashboard_button)

		self.additional_tasks_button = Button(width=100, height=100, text='Additional Tasks',
											  image=self.additional_tasks)
		self.canvas2.create_window(600, 220, window=self.additional_tasks_button)

		self.manager_area_text = self.canvas2.create_text(450, 100, text="Manager Area", font=("Arial", 15, "bold"))
		self.register_new_staff_text = self.canvas2.create_text(300, 290, text="Register New Staff", font=("Arial", 10, "bold"))
		self.staff_dashboard_text = self.canvas2.create_text(448, 290, text="Staff Dashboard", font=("Arial", 10, "bold"))
		self.additional_tasks_text = self.canvas2.create_text(600, 290, text="Additional Tasks", font=("Arial", 10, "bold"))

		self.window.mainloop()

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
		from manager_login_UI import ManagerLoginUI
		ManagerLoginUI()

	def go_to_staff_dashboard(self):
		self.window.destroy()
		from staff.staff_dashboard_UI import StaffDashboard_UI
		StaffDashboard_UI()


ManagerDashboardUI()
