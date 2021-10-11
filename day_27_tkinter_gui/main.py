import tkinter

window = tkinter.Tk()

window.title('Mi to Km App')
window.minsize(height=300, width=400)

my_label = tkinter.Label(text='Miles to Kilometers App', font=('Arial', 20, 'normal'))
my_label.pack()


window.mainloop()
