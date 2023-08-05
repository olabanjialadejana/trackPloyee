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


window = Tk()
window.title("TrackPloyee")
window.geometry("900x600")
window.config(background="#27374D")

canvas = Canvas(width=900, height=150)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(450, 100, image=logo_img)
canvas.config(background="#DDE6ED")
canvas.grid(column=0, row=0)

canvas2 = Canvas(width=900, height=450)
canvas2.create_rectangle(210, 400, 690, 50, fill="#9DB2BF")
canvas2.config(background="#526D82")
initial_time = datetime.datetime.now().strftime('%I:%M %p')
initial_date = datetime.datetime.now().strftime('%A, %B %d')
date_text = canvas2.create_text(450, 200, text=initial_date, font=("Arial", 10))
time_text = canvas2.create_text(450, 150, text=initial_time, font=("Arial", 24))
canvas2.grid(column=0, row=1)

# Username Entry
username_entry = Entry(width=32, fg='grey')
username_entry.focus()
username_entry.insert(0, "Username")
canvas2.create_window(450, 230, window=username_entry)

# Password Entry
password_entry = Entry(width=32, fg='grey')
password_entry.focus()
password_entry.insert(0, "Password")
canvas2.create_window(450, 260, window=password_entry)



update_time()

window.mainloop()
