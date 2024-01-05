from tkinter import *

root = Tk()
root.geometry('300x300')
root.title('test')

#labels
name_lbl = Label(root , text = 'Name :')
name_lbl.place(x= 20 , y = 10)

family_lbl = Label(root , text = 'Family :')
family_lbl.place(x= 20 , y = 50)

salary_lbl = Label(root , text = 'Salary :')
salary_lbl.place(x= 20 , y = 90)

#entries
name_entry = Entry(root , )
name_entry.place(x = 100 , y = 10)

family_entry = Entry(root , )
family_entry.place(x = 100 , y = 50)

salary_entry = Entry(root , )
salary_entry.place(x = 100 , y = 90)

#buttons
tax_btn = Button(root , text='Tax' , width=8)
tax_btn.place(x = 80 , y = 140)

insure_btn = Button(root , text='Insure' , width=8)
insure_btn.place(x = 150 , y = 140)

status_btn = Button(root , text='Status' , width=8)
status_btn.place(x = 80 , y = 180)

exit_btn = Button(root , text='Exit' , width=8)
exit_btn.place(x = 150 , y = 180)


























root.mainloop()






































