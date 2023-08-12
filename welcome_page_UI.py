from tkinter import *


def open_password_login():
	window.destroy()
	from login_UI import launch_login_UI


window = Tk()
window.title("TrackPloyee")
window.geometry("900x600")
window.config(background="#27374D")

canvas = Canvas(width=900, height=150, background="#DDE6ED")
logo_img = PhotoImage(file="logo.png")
canvas.create_image(450, 100, image=logo_img)
canvas.grid(column=0, row=0)

canvas2 = Canvas(width=900, height=450, background="#526D82")
canvas2.create_rectangle(210, 400, 690, 50, fill="#9DB2BF")
canvas2.grid(column=0, row=1)

password_img = PhotoImage(file="samples/welcome-page-logos/icons8-password-window-100.png")
fingerprint_img = PhotoImage(file="samples/welcome-page-logos/icons8-fingerprint-scan-64.png")
facial_recognition_img = PhotoImage(file="samples/welcome-page-logos/icons8-facial-recognition-100.png")
manager_img = PhotoImage(file="samples/welcome-page-logos/icons8-manager-100.png")
new_employee_img = PhotoImage(file="samples/welcome-page-logos/icons8-add-user-male-female-100.png")

password_login_button = Button(width=100, height=100, text='Password Login', image=password_img,
							   command=open_password_login)
canvas2.create_window(300, 150, window=password_login_button)

fingerprint_login_button = Button(width=100, height=100, text='Fingerprint Login', image=fingerprint_img)
canvas2.create_window(450, 150, window=fingerprint_login_button)

facial_recognition_login_button = Button(width=100, height=100, text='Facial Recognition Login',
										 image=facial_recognition_img)
canvas2.create_window(600, 150, window=facial_recognition_login_button)

new_employee_registration_button = Button(width=100, height=100, text='New Employee Registration',
										  image=new_employee_img)
canvas2.create_window(550, 300, window=new_employee_registration_button)

manager_login_button = Button(width=100, height=100, text='Manager Login', image=manager_img)
canvas2.create_window(380, 300, window=manager_login_button)

window.mainloop()
