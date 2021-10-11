from tkinter import *

default_output = 'mi'
window = Tk()

window.title('Mi to Km App')
window.minsize(height=300, width=400)

# create texts
app_name = Label(text='Miles to Kilometers App', font=('Arial', 20, 'normal'))
app_name.pack()

# create input fields
calc_input = Entry(width=10)
calc_input.pack()
calc_input.get()

# calc_input.insert(END, string="km")
equal_sign = Label(text='=', font=('Arial', 20, 'normal'))
equal_sign.pack()

calc_output = Entry(width=10)
calc_output.pack()
calc_output.get()
# calc_output.insert(END, string=default_output)


# create buttons
def button_clicked():
    global default_output
    num = int(calc_input.get())
    num /= 1.609
    str(num)
    calc_output.insert(END, string=num)


button = Button(text='calc', command=button_clicked)
button.pack()

window.mainloop()
