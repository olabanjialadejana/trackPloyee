from tkinter import *
from tkinter import messagebox
import datetime


def launch_login_UI():
	def update_time():
		# This function updates the screen time function
		now = datetime.datetime.now()
		current_date = now.strftime('%A, %B %d')
		current_time = now.strftime('%I:%M %p')
		canvas2.itemconfig(time_text, text=current_time)
		canvas2.itemconfig(date_text, text=current_date)

	def show_password_entry(event):
		# This function shows password entry
		canvas2.create_window(450, 260, window=password_entry)
		canvas2.create_window(403, 285, window=check_button_frame)
		check_button.pack()
		canvas2.create_window(507, 310, window=login_button)

	def clear_username(event):
		# clear username
		if username_entry.get() == "Username":
			username_entry.delete(0, END)
			username_entry.config(fg="black")  # Set text color to black when typing starts

	def clear_password(event):
		# clear initial password entry
		password_entry.delete(0, END)
		password_entry.config(show="*", fg="black")  # Set text color to black when typing starts

	def toggle_showing_password():
		if check_var.get() == 1:
			password_entry.config(show='')
		else:
			password_entry.config(show='*')

	def messageOnClickLogin():
		# message box (either welcome info or log in error)
		now = datetime.datetime.now()
		current_time = now.strftime('%I:%M %p')
		messagebox.showinfo(title="Login successful!!", message=f"Login time:{current_time}\nWelcome to Work!!!!")
		messagebox.showerror(title="login not successful", message="User not found in system")

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

	# Set the initial time and date for initial display in canvas2
	initial_time = datetime.datetime.now().strftime('%I:%M %p')
	initial_date = datetime.datetime.now().strftime('%A, %B %d')
	date_text = canvas2.create_text(450, 200, text=initial_date, font=("Arial", 10))
	time_text = canvas2.create_text(450, 150, text=initial_time, font=("Arial", 24))
	canvas2.grid(column=0, row=1)

	# Username Entry
	username_entry = Entry(width=32, fg='grey')
	username_entry.insert(0, "Username")
	canvas2.create_window(450, 230, window=username_entry)

	# Bind the Enter key press event to the show_password_entry only after entering username and pressing "ENTER"
	username_entry.bind("<FocusIn>", clear_username)
	username_entry.bind("<Return>", show_password_entry)
	# username_entry.bind("<Return>", show_tick_box)

	# Password Entry
	password_entry = Entry(width=32, fg='grey')
	password_entry.insert(0, "Password")
	password_entry.bind("<FocusIn>", clear_password)

	# Tick box
	check_button_frame = Frame(canvas2, bg="#9DB2BF")
	check_var = IntVar()
	check_button = Checkbutton(check_button_frame,
							   text='Show password',
							   variable=check_var,
							   bg="#9DB2BF",
							   command=toggle_showing_password)

	# Login button
	login_button = Button(width=10, text='Login', command=messageOnClickLogin)

	# keep updating the time and date in canvas2
	update_time()

	window.mainloop()

launch_login_UI()