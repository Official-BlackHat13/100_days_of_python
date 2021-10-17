from tkinter import *
from tkinter import messagebox
from password_generator import generate_password

FONT_NAME = "Courier"


# ----------------------- PASSWORD GENERATOR ----------------------- #
def pass_password():
    password = generate_password()
    password_input.delete(0, END)
    password_input.insert(0, password)


# ----------------------- SAVE PASSWORD ----------------------- #

def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='hey fuckface!', message='enter something!')
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'r u sure?')

        if is_ok:
            with open('data.txt', 'a') as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ----------------------- UI SETUP ----------------------- #

# creating window
window = Tk()
window.title('Password manager')
window.config(padx=50, pady=50, bg='white')

# creating canvas
canvas = Canvas(width=200, height=200, bg='white', highlightthickness=0)

# adding image
lock_image = PhotoImage(file='lock.png')
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# creating input fields and belonging text


# -- website field -- #

# text
website_label = Label(text='website:', font=(FONT_NAME, 14), bg='white')
website_label.grid(row=1, column=0)

# input
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

# -- email/username field -- #

# text
username_label = Label(text='email/username:', font=(FONT_NAME, 14), bg='white')
username_label.grid(row=2, column=0)

# input
username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)
username_input.insert(0, 'huba0ferencz@gmail.com')

# -- password field -- #

# text
password_label = Label(text='password:', font=(FONT_NAME, 14), bg='white')
password_label.grid(row=3, column=0)

# output
password_input = Entry(width=35)
password_input.grid(row=3, column=1, columnspan=2)

# button
generate_button = Button(text='generate', bg='#f0f0f0', command=pass_password)
generate_button.grid(row=3, column=2, columnspan=2)

# -- submit field -- #

# button

add_button = Button(text='add', width=32, bg='#f0f0f0', command=save)
add_button.grid(row=4, column=1, columnspan=2)
window.mainloop()
