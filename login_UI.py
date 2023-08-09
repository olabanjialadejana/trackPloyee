from tkinter import *
import datetime


# ------------------------------------ SCREEN TIME FUNCTION ------------------------------------ #
def update_time():
	now = datetime.datetime.now()
	current_date = now.strftime('%A, %B %d')
	current_time = now.strftime('%I:%M %p')
	# make canvas2 a global variable in this function
	canvas2.itemconfig(time_text, text=current_time)
	canvas2.itemconfig(date_text, text=current_date)
	# Update the time after every 1000 milliseconds (1 second)
	window.after(1000, update_time)


# ------------------------------------ SCREEN TIME FUNCTION ------------------------------------ #

# ------------------------------------ SHOW PASSWORD ENTRY ------------------------------------- #
def show_password_entry(event):
	canvas2.create_window(450, 260, window=password_entry)


# ------------------------------------ SHOW PASSWORD ENTRY ------------------------------------- #

# ------------------------------------ CLEAR USERNAME      ------------------------------------- #
def clear_username(event):
	if username_entry.get() == "Username":
		username_entry.delete(0, END)
		username_entry.config(fg="black")  # Set text color to black when typing starts

# ------------------------------------ CLEAR USERNAME  ------------------------------------- #

# ------------------------------------ CLEAR INITIAL PASSWORD ENTRY ------------------------------------- #
def clear_password(event):
	password_entry.delete(0, END)
	password_entry.config(show="*", fg="black")  # Set text color to black when typing starts

# ------------------------------------ CLEAR INITIAL PASSWORD ENTRY ------------------------------------- #

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

# Password Entry
password_entry = Entry(width=32, fg='grey')
password_entry.insert(0, "Password")
password_entry.bind("<FocusIn>", clear_password)

# Function to keep updating the time and date in canvas2
update_time()

window.mainloop()
