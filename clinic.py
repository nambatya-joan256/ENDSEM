from tkinter import *
import tkinter as tk
import datetime
import time
from tkinter import ttk
import sqlite3
from tkinter import messagebox


headlabelfont = ("Noto Sans CJK TC", 15, 'bold')
labelfont = ('Arial', 14, 'bold')
entryfont = ('Arial', 15, 'bold')

connector = sqlite3.connect('clinic.db')
cursor = connector.cursor()
connector.execute(
"CREATE TABLE IF NOT EXISTS clinic (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NAME TEXT, EMAIL TEXT, PHONE_NO TEXT, GENDER TEXT, MEDICINE TEXT)"
)

def display_records():
    cursor.execute('SELECT * FROM clinic')
    records = cursor.fetchall()
    for record in records:
        tree.insert('', 'end', values=record)


def add_record():
    global name_strvar, email_strvar, contact_strvar, gender_strvar, medicine
    name = name_strvar.get()
    email = email_strvar.get()
    contact = contact_strvar.get()
    gender = gender_strvar.get()
    #DOB = dob.get_date()
    medicine = medicine_strvar.get()
    if not name or not email or not contact or not gender or not medicine:
        messagebox.showerror('Error!', "Please fill all the missing fields!!")
    else:
        try:
            connector.execute(
            'INSERT INTO clinic (NAME, EMAIL, PHONE_NO, GENDER, MEDICINE) VALUES (?,?,?,?,?)', (name, email, contact, gender, medicine)
            )
            connector.commit()
            messagebox.showinfo('Record added', f"Record of {name} was successfully added")
            #reset_fields()
            display_records()
        except:
            messagebox.showerror('Wrong type', 'The type of the values entered is not accurate.\n Pls note that the contact field can only contain numbers')


main = Tk()
main.title("Clinic Management System")
main.geometry('1000x600')
main.resizable(1,1)

lf_bg = 'green'

name_strvar = StringVar()
email_strvar = StringVar()
contact_strvar = StringVar()
gender_strvar = StringVar()
medicine_strvar = StringVar()

Label(main, text="Clinic Management System", font=("arial bold",18), bg='Blue',fg='white').pack(side=TOP, fill=X)
left_frame = Frame(main, bg=lf_bg)
left_frame.place(x=0, y=30, relheight=1, relwidth=0.3)
#center_frame = Frame(main, bg=cf_bg)
#center_frame.place(relx=0.2, y=30, relheight=1, relwidth=0.2)
right_frame = Frame(main, bg="white")
right_frame.place(relx=0.3, y=30, relheight=1, relwidth=0.8)

Label(left_frame,text="Name", font=("arial ",12),bg=lf_bg).place(relx=0.075, rely=0.05)
Label(left_frame, text="Contact Number", font=("arial ",12), bg=lf_bg).place(relx=0.075, rely=0.18)
Label(left_frame, text="Email Address", font=("arial ",12), bg=lf_bg).place(relx=0.072, rely=0.31)
Label(left_frame, text="Gender", font=("arial ",12), bg=lf_bg).place(relx=0.075, rely=0.44)
Label(left_frame, text="medicine", font=("arial ",12), bg=lf_bg).place(relx=0.073, rely=0.57)
#Label(left_frame, text="Stream", font=("arial ",12), bg=lf_bg).place(relx=0.3, rely=0.7)
Entry(left_frame, width=19, textvariable=name_strvar, font=("arial ",12)).place(x=20, rely=0.1)
Entry(left_frame, width=19, textvariable=contact_strvar, font=("arial ",12)).place(x=20, rely=0.23)
Entry(left_frame, width=19, textvariable=email_strvar, font=("arial ",12)).place(x=20, rely=0.36)
#Entry(left_frame, width=19, textvariable=medicine_strvar, font=("arial ",12)).place(x=20, rely=0.62)
OptionMenu(left_frame, gender_strvar, 'Male', "Female").place(x=20, rely=0.49, relwidth=0.5)
OptionMenu(left_frame, medicine_strvar, 'panado', "Dexona","Dichlophenac","Metro","").place(x=20, rely=0.63, relwidth=0.7)

Button(left_frame, text='Submit', bg='orange', font=('arial bold',15), command=add_record, width=16).place(relx=0.15, rely=0.75)


# def reset_fields():
#     global name_strvar, email_strvar, contact_strvar, gender_strvar, medicine_strvar
#     for i in ['name_strvar', 'email_strvar', 'contact_strvar', 'gender_strvar', 'stream_strvar']:
#         exec(f"{i}.set('')")
#     #dob.set_date(datetime.datetime.now().date())
# def reset_form():
#     global tree
#     tree.delete(*tree.get_children())
#     reset_fields()
# def display_records():
#     tree.delete(*tree.get_children())
#     curr = connector.execute('SELECT * FROM SCHOOL_MANAGEMENT')
#     data = curr.fetchall()
# for records in data:
#     tree.insert('', END, values=records)
    

Label(right_frame, text='Patient Record', font=headlabelfont, bg='red', fg='LightCyan').pack(side=TOP, fill=X)
tree = ttk.Treeview(right_frame, height=100, selectmode=BROWSE,
                    columns=('ID', "Name", "Email Address", "Contact Number", "Gender", "medicine"))
X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)
X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)
tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)
tree.heading('ID', text='ID', anchor=CENTER)
tree.heading('Name', text='Name', anchor=CENTER)
tree.heading('Email Address', text='Email ID', anchor=CENTER)
tree.heading('Contact Number', text='Phone No', anchor=CENTER)
tree.heading('Gender', text='Gender', anchor=CENTER)
#tree.heading('Date of Birth', text='DOB', anchor=CENTER)
tree.heading('medicine', text='medicine', anchor=CENTER)
tree.column('#0', width=0, stretch=NO)
tree.column('#1', width=40, stretch=NO)
tree.column('#2', width=140, stretch=NO)
tree.column('#3', width=200, stretch=NO)
tree.column('#4', width=80, stretch=NO)
tree.column('#5', width=80, stretch=NO)
#tree.column('#6', width=80, stretch=NO)
tree.column('#6', width=150, stretch=NO)
tree.place(y=30, relwidth=1, relheight=0.9, relx=0)
display_records()




main.update()
main.mainloop()