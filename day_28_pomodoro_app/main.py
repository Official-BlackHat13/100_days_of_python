from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#FF6D3A"
RED = "#FF4C4C"
GREEN = "#3D6687"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
message = 'timer'
color = GREEN
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    title_label.config(text='timer')
    check_marks.config(text='')
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def work_min():
    count_down(WORK_MIN * 60)


def short_break_min():
    count_down(SHORT_BREAK_MIN * 60)


def long_break_min():
    count_down(LONG_BREAK_MIN * 60)


def start_timer():
    global reps
    global message
    global color
    reps += 1
    if reps % 8 == 0:
        title_label.config(text='break', fg=RED)
        long_break_min()
    elif reps % 2 == 0:
        title_label.config(text='break', fg=PINK)
        short_break_min()
    else:
        title_label.config(text='work', fg=GREEN)
        work_min()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_minute = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        marks = ''
        start_timer()
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            marks += '✔'
            check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

# creating window
window = Tk()
window.title('Pomodoro App')
window.config(padx=50, pady=25, bg=YELLOW)
window.maxsize(400, 400)

# adding app title
title_label = Label(text=message, fg=color, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# adding image as canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='stopwatch.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='#0D5177', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

# creating buttons
start_button_img = PhotoImage(file='start.png')
start_button_img_label = Label(image=start_button_img)

start_button = Button(image=start_button_img, bg=YELLOW, command=start_timer, highlightthickness=0, borderwidth=0)
start_button.grid(column=0, row=2)

reset_button_img = PhotoImage(file='stop-button.png')
reset_button_img_label = Label(image=reset_button_img)

reset_button = Button(image=reset_button_img, bg=YELLOW, command=reset_timer, highlightthickness=0, borderwidth=0)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
