from tkinter import *
from tkinter import messagebox
import datetime


class LoginUI:
    def __init__(self):
        self.window = Tk()
        self.window.title("TrackPloyee")
        self.window.geometry("900x600")
        self.window.config(background="#27374D")
        self.canvas = Canvas(width=900, height=150, background="#DDE6ED")
        self.logo_img = PhotoImage(file="../images/logo.png")
        self.canvas.create_image(450, 100, image=self.logo_img)
        self.canvas.grid(column=0, row=0)
        self.go_back_img = PhotoImage(file="../images/icons8-go-back-48.png")
        self.go_back_button = Button(width=48, height=48, text='go_back',
        							 image=self.go_back_img, command=self.go_back_to_welcome_page)
        # Position the button at the upper left part of the canvas
        self.canvas.create_window(10, 10, anchor="nw", window=self.go_back_button)
        self.canvas2 = Canvas(width=900, height=450, background="#526D82")
        self.canvas2.create_rectangle(210, 400, 690, 50, fill="#9DB2BF")
        self.initial_time = datetime.datetime.now().strftime('%I:%M %p')
        self.initial_date = datetime.datetime.now().strftime('%A, %B %d')
        self.date_text = self.canvas2.create_text(450, 200, text=self.initial_date, font=("Arial", 10))
        self.time_text = self.canvas2.create_text(450, 150, text=self.initial_time, font=("Arial", 24))
        self.canvas2.grid(column=0, row=1)
        self.username_entry = Entry(width=32, fg='grey')
        self.username_entry.insert(0, "Username")
        self.canvas2.create_window(450, 230, window=self.username_entry)
        self.username_entry.bind("<FocusIn>", self.clear_username)
        self.username_entry.bind("<Return>", self.show_password_entry)
        self.password_entry = Entry(width=32, fg='grey')
        self.password_entry.insert(0, "Password")
        self.password_entry.bind("<FocusIn>", self.clear_password)
        self.check_button_frame = Frame(self.canvas2, bg="#9DB2BF")
        self.check_var = IntVar()
        self.check_button = Checkbutton(self.check_button_frame,
                                        text='Show password',
                                        variable=self.check_var,
                                        bg="#9DB2BF",
                                        command=self.toggle_showing_password)
        self.login_button = Button(width=10, text='Login', command=self.messageOnClickLogin)
        self.update_time()
        self.window.mainloop()

    def update_time(self):
        now = datetime.datetime.now()
        current_date = now.strftime('%A, %B %d')
        current_time = now.strftime('%I:%M %p')
        self.canvas2.itemconfig(self.time_text, text=current_time)
        self.canvas2.itemconfig(self.date_text, text=current_date)

    def show_password_entry(self, event):
        self.canvas2.create_window(450, 260, window=self.password_entry)
        self.canvas2.create_window(403, 285, window=self.check_button_frame)
        self.check_button.pack()
        self.canvas2.create_window(507, 310, window=self.login_button)

    def clear_username(self, event):
        if self.username_entry.get() == "Username":
            self.username_entry.delete(0, END)
            self.username_entry.config(fg="black")

    def clear_password(self, event):
        self.password_entry.delete(0, END)
        self.password_entry.config(show="*", fg="black")

    def toggle_showing_password(self):
        if self.check_var.get() == 1:
            self.password_entry.config(show='')
        else:
            self.password_entry.config(show='*')

    def messageOnClickLogin(self):
        now = datetime.datetime.now()
        current_time = now.strftime('%I:%M %p')
        messagebox.showinfo(title="Login successful!!", message=f"Login time: {current_time}\nWelcome to Work!!!!")
        messagebox.showerror(title="login not successful", message="User not found in system")

    def go_back_to_welcome_page(self):
        self.window.destroy()
        from welcome_page.welcome_page_UI import WelcomePageUI
        WelcomePageUI()
