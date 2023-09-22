from tkinter import *


class LoginUIOptions:
	def __init__(self):
		self.window = Tk()
		self.window.title("Login Options")
		self.window.geometry("900x600")
		self.window.config(background="#27374D")
		self.canvas = Canvas(width=900, height=150, background="#DDE6ED")
		self.logo_img = PhotoImage(file="../images/logo.png")
		self.canvas.create_image(450, 100, image=self.logo_img)
		self.canvas.grid(column=0, row=0)
		self.canvas2 = Canvas(width=900, height=450, background="#526D82")
		self.canvas2.create_rectangle(210, 400, 690, 50, fill="#9DB2BF")
		self.canvas2.grid(column=0, row=1)
		self.theme_text = self.canvas2.create_text(450, 100, text="Choose a Login Method", font=("Arial", 15, "bold"))
		self.password_img = PhotoImage(file="../images/icons8-password-window-100.png")
		self.fingerprint_img = PhotoImage(file="../images/icons8-fingerprint-scan-64.png")
		self.facial_recognition_img = PhotoImage(file="../images/icons8-facial-recognition-100.png")

		self.coming_soon_img = PhotoImage(file="../images/icons8-coming-soon-100.png")

		self.password_login_button = Button(width=100, height=100, text='Password Login', image=self.password_img,
											command=self.open_password_login)
		self.canvas2.create_window(300, 210, window=self.password_login_button)
		self.fingerprint_login_button = Button(width=100, height=100, text='Fingerprint Login',
											   image=self.fingerprint_img)
		self.canvas2.create_window(450, 210, window=self.fingerprint_login_button)
		self.canvas2.create_image(450, 281, image=self.coming_soon_img)
		self.facial_recognition_login_button = Button(width=100, height=100, text='Facial Recognition Login',
													  image=self.facial_recognition_img)

		self.canvas2.create_window(600, 210, window=self.facial_recognition_login_button)
		self.canvas2.create_image(600, 281, image=self.coming_soon_img)

		self.go_back_img = PhotoImage(file="../images/icons8-go-back-48.png")
		self.go_back_button = Button(width=48, height=48, text='go_back',
									 image=self.go_back_img, command=self.go_back_to_welcome_page)
		# Position the button at the upper left part of the canvas
		self.canvas.create_window(10, 10, anchor="nw", window=self.go_back_button)


		self.window.mainloop()

	def open_password_login(self):
		self.window.destroy()
		from login.login_UI import LoginUI
		LoginUI()

	def open_staff_registration(self):
		self.window.destroy()
		from staff.staff_registration_UI import StaffRegistrationUI
		StaffRegistrationUI()

	def go_back_to_welcome_page(self):
		self.window.destroy()
		from welcome_page.welcome_page_UI import WelcomePageUI
		WelcomePageUI()



