from tkinter import *
from tkinter import ttk
# from login_UI_options import WelcomePageUI this will be the link to the manager dashboard
import json
import os
from tkinter import messagebox

# Get the absolute path to the directory containing this script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate to the image directory from the script's location
image_dir = os.path.join(script_dir, "..", "images")

os.chdir(image_dir)



class StaffDashboard_UI:
    def __init__(self):
        self.window = Tk()
        self.window.title("Admin Dashboard")
        self.window.geometry("983x600")
        self.window.config(background="#27374D")

        self.canvas = Canvas(width=980, height=100, background="#DDE6ED")
        self.logo_img = PhotoImage(file="logo.png")
        self.canvas.create_image(490, 50, image=self.logo_img)
        self.canvas.grid(column=0, row=0)

        self.go_back_img = PhotoImage(file="icons8-go-back-48.png")
        self.go_back_button = Button(width=48, height=48, text='go_back',
                                     image=self.go_back_img, command=self.go_back_to_manager_dashboard)
        # Position the button at the upper left part of the canvas
        self.canvas.create_window(10, 10, anchor="nw", window=self.go_back_button)

        self.canvas2 = Canvas(width=980, height=500, background="#526D82")
        self.canvas2.create_rectangle(8, 500, 980, 8, fill="#9DB2BF")
        self.canvas2.grid(column=0, row=1)

        # Create a custom style for column headers
        bold_font = ('TkDefaultFont', 10, 'bold')  # Change the font size and style as needed
        style = ttk.Style()
        style.configure("Bold.Treeview.Heading", font=bold_font)

        # Create the table (treeview)
        self.table = ttk.Treeview(columns=(
            'staff_number', 'first_name', 'last_name', 'age', 'telephone', 'email', 'password', 'department_unit', 'position',
            'pay'),
            show='headings', style="Bold.Treeview")
        self.table.heading('staff_number', text='Staff Number')
        self.table.heading('first_name', text='First Name')
        self.table.heading('last_name', text='Last Name')
        self.table.heading('age', text='Age')
        self.table.heading('telephone', text='Telephone')
        self.table.heading('email', text='Email')
        self.table.heading('password', text='Password')
        self.table.heading('department_unit', text='Department/Unit')
        self.table.heading('position', text='Position')
        self.table.heading('pay', text='Pay')

        # Define the column widths to fit within the rectangle
        self.table.column('staff_number', width=90)
        self.table.column('first_name', width=110)
        self.table.column('last_name', width=100)
        self.table.column('age', width=40)
        self.table.column('telephone', width=100)
        self.table.column('email', width=150)
        self.table.column('password', width=60)
        self.table.column('department_unit', width=120)
        self.table.column('position', width=100)
        self.table.column('pay', width=95)

        self.canvas2.create_window(10, 20, anchor="nw", window=self.table)  # Adjust the coordinates as needed

        self.load_data_from_json()

        self.window.mainloop()

    def go_back_to_manager_dashboard(self):
        self.window.destroy()
        from manager.manager_dashboard_UI import ManagerDashboardUI
        ManagerDashboardUI()

    def load_data_from_json(self):
        try:
            with open('../database/data.json', 'r') as json_file:
                data = json.load(json_file)
                for staff_number, values in data.items():
                    # Exclude 'address', 'next of kin', 'next of kin address', 'next of kin telephone'
                    values.pop('address', None)
                    values.pop('next of kin', None)
                    values.pop('next of kin address', None)
                    values.pop('next of kin telephone', None)
                    self.table.insert("", "end", values=(
                        staff_number, values["first name"], values["last name"], values["age"], values["telephone"],
                        values["email"], values["password"], values["department/unit"], values["position"], values["pay"]))
        except FileNotFoundError:
            messagebox.showerror(title="Database Error!!!", message="No user database yet!!!")



