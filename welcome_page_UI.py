from tkinter import *


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
		self.password_img = PhotoImage(file="samples/welcome-page-logos/icons8-password-window-100.png")
		self.fingerprint_img = PhotoImage(file="samples/welcome-page-logos/icons8-fingerprint-scan-64.png")
		self.facial_recognition_img = PhotoImage(file="samples/welcome-page-logos/icons8-facial-recognition-100.png")
		self.manager_img = PhotoImage(file="samples/welcome-page-logos/icons8-manager-100.png")
		self.new_employee_img = PhotoImage(file="samples/welcome-page-logos/icons8-add-user-male-female-100.png")
		self.coming_soon_img = PhotoImage(file="samples/welcome-page-logos/icons8-coming-soon-100.png")

		self.password_login_button = Button(width=100, height=100, text='Password Login', image=self.password_img,
											command=self.open_password_login)
		self.canvas2.create_window(300, 150, window=self.password_login_button)
		self.fingerprint_login_button = Button(width=100, height=100, text='Fingerprint Login',
											   image=self.fingerprint_img)
		self.canvas2.create_window(450, 150, window=self.fingerprint_login_button)
		self.canvas2.create_image(450, 221, image=self.coming_soon_img)
		self.facial_recognition_login_button = Button(width=100, height=100, text='Facial Recognition Login',
													  image=self.facial_recognition_img)

		self.canvas2.create_window(600, 150, window=self.facial_recognition_login_button)
		self.canvas2.create_image(600, 221, image=self.coming_soon_img)
		self.new_employee_registration_button = Button(width=100, height=100, text='New Employee Registration',
													   image=self.new_employee_img)
		self.canvas2.create_window(550, 320, window=self.new_employee_registration_button)
		self.manager_login_button = Button(width=100, height=100, text='Manager Login', image=self.manager_img)
		self.canvas2.create_window(380, 320, window=self.manager_login_button)

		self.window.mainloop()

	def open_password_login(self):
		self.window.destroy()
		from login_UI import LoginUI
		LoginUI()



