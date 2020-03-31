from tkinter import *

root = Tk()
root.title("Police Computer Pro XS Max")
root.geometry("700x500")

title = Label(text="Police Department Database System", fg="#0000CD", font="Colonas 15")
title.pack()

def name_check():
	name = search.get()
	label_name = Label(text=name, fg="#0000CD", font="Colonas")
	label_name.place(x=300, y=150)

	label1 = Label(text="Information about ", fg="#0000CD", font="Colonas")
	label1.place(x=136, y=150)

	info1 = Label(text="Home adress: LA, 332 N.Hollywood", fg="#0000CD", font="Colonas")
	info1.place(y=177)
	info2 = Label(text="Gun licence: YES", fg="#0000CD", font="Colonas")
	info2.place(y=210)
	info3 = Label(text="Arrest/Search warrants: NO", fg="#0000CD", font="Colonas")
	info3.place(y=247)

def licence_check():
	licence_checked = licence.get()
	label_licence = Label(text=licence_checked, fg="#0000CD", font="Colonas")
	label_licence.place(x=300, y=300)

	label2 = Label(text="Information about ", fg="#0000CD", font="Colonas")
	label2.place(x=136, y=300)

	info4 = Label(text="Owner name: Richard Hernandes", fg="#0000CD", font="Colonas")
	info4.place(y=320)
	info5 = Label(text="Validation of LP: VALID", fg="#0000CD", font="Colonas")
	info5.place(y=360)
	info6 = Label(text="Date of registration: 06/23/2015", fg="#0000CD", font="Colonas")
	info6.place(y=400)
	info7 = Label(text="Wanted: YES", fg="red", font="Colonas")
	info7.place(y=430)

# name check
enter_name = Label(text="Enter name for get information: ", fg="#0000CD", font="Colonas")
enter_name.place(y=60)

search = StringVar()
search_entry = Entry(textvariable=search)
search_entry.place(x=300, y=60)

search_button = Button(text="Search", command=name_check)
search_button.place(x=500, y=55)

#licence plate check
enter_name = Label(text="Enter licence plate for get information: ", fg="#0000CD", font="Colonas")
enter_name.place(y=100)

licence = StringVar()
search_entry = Entry(textvariable=licence)
search_entry.place(x=350, y=100)

search_button_lp = Button(text="Search", command=licence_check)
search_button_lp.place(x=550, y=95)

# code buttons
code2 = Button(text="CODE 2", fg='#FFA500')
code2.place(x=420, y=460)

code3 = Button(text="CODE 3", fg='#FF4500')
code3.place(x=500, y=460)

code4 = Button(text="CODE 4", fg='green')
code4.place(x=580, y=460)

panic = Button(text="PANIC", fg='red')
panic.place(x=350, y=460)

root.mainloop()


# created by h4cktivist