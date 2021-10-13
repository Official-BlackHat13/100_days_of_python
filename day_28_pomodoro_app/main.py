from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    current_time = WORK_MIN
    if reps
    count_down(current_time * 60)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_minute = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

# creating window
window = Tk()
window.title('Pomodoro App')
window.config(padx=100, pady=50, bg=YELLOW)

# adding app title
title_label = Label(text='timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# adding image as canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# creating buttons
start_button = Button(text='start', command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text='reset', highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = Label(text='✔', fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
