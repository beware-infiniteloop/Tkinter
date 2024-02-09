from tkinter import *
from tkcalendar import Calendar

root = Tk()
root.geometry('500x500')
root.title("Hotel Registration Form")

sname = Label(root, text='Enter Your Name')
n = Label(root, text='Enter Number of guests')
in_date = Label(root, text="Enter Check-in date:")
out_date = Label(root, text="Enter Check-out date:")
room_type_label = Label(root, text='Enter room preference')

sname.grid()
n.grid(row=1)
in_date.grid(row=3)
out_date.grid(row=4)
room_type_label.grid(row=6)

name_value = StringVar()
n_value = StringVar()
in_cal = Calendar(root, selectmode='day', year=2024, month=1, day=1)
out_cal = Calendar(root, selectmode='day', year=2024, month=1, day=1)
room_type_var = StringVar()

userentry = Entry(root, textvariable=name_value)
nentry = Entry(root, textvariable=n_value)

single_check = Checkbutton(root, text="Single", variable=room_type_var, onvalue="Single", offvalue="")
double_check = Checkbutton(root, text="Double", variable=room_type_var, onvalue="Double", offvalue="")
suite_check = Checkbutton(root, text="Suite", variable=room_type_var, onvalue="Suite", offvalue="")
other_check = Checkbutton(root, text="Other", variable=room_type_var, onvalue="Other", offvalue="")

userentry.grid(row=0, column=1)
nentry.grid(row=1, column=1)
in_cal.grid(row=3, column=1)
out_cal.grid(row=4, column=1)
single_check.grid(row=6, column=1)
double_check.grid(row=6, column=2)
suite_check.grid(row=6, column=3)
other_check.grid(row=6, column=4)

def getvals():
    with open('Hotel_entries.txt', 'a') as f:
        f.write(f"Name: {name_value.get()}, Guests: {n_value.get()}, Check-in: {in_cal.get_date()}, "
                f"Check-out: {out_cal.get_date()}, Room Type: {room_type_var.get()}\n")
    root.quit()
    print('You have registered successfully!')

Button(text='Submit', command=getvals).grid()

root.mainloop()
