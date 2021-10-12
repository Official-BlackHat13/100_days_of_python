from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro App')
window.config(padx=0, pady=0)
canvas = Canvas(width=800, height=520, highlightthickness=0)
bg_image = PhotoImage(file='making-timer-in-scratch-coding.png')
canvas.create_image(400, 260, image=bg_image)
canvas.create_text(400, 310, text='00:00', fill='black', font=(FONT_NAME, 37, 'bold'))
canvas.pack()

window.mainloop()
