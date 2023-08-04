from tkinter import *
import datetime


# ------------------------------------ SCREEN TIME FUNCTION ------------------------------------ #
def update_time():
	now = datetime.datetime.now()
	# current_time = now.strftime("%H:%M:%S\n%d/%m/%Y")
	current_time = now.strftime('%H:%M:%S\n%A, %B %d')
	# make canvas2 a global variable in this function
	canvas2.itemconfig(time_text, text=current_time)
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
# initial_time = datetime.datetime.now().strftime("%H:%M:%S\n%d/%m/%Y")
initial_time = datetime.datetime.now().strftime('%H:%M:%S\n%A, %B %d')
time_text = canvas2.create_text(450, 225, text=initial_time, font=("Arial", 24))
canvas2.grid(column=0, row=1)



update_time()

window.mainloop()
