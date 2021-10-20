from tkinter import *

# ----------- CONSTANTS ----------- #
BACKGROUND_COLOR = '#c7ffd5'

# ----------- UI ----------- #
window = Tk()
window.title('most used korean words')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=800)
flash_card = PhotoImage(file='media/flashcard.png')
canvas.create_image(400, 400, image=flash_card)
# korean text
canvas.create_text(400, 140, text='Korean', font=('Ariel', 40, 'italic'))
# korean pronunciation
canvas.create_text(400, 280, text='pronunciation', font=('Ariel', 40, 'italic'))
# english
canvas.create_text(400, 590, text='English', font=('Ariel', 40, 'italic'))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=1)

cross_image = PhotoImage(file='media/wrong_button.png')
unknown_button = Button(image=cross_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0)
unknown_button.grid(row=0, column=0)

checkmark_image = PhotoImage(file='media/right_button.png')
known_button = Button(image=checkmark_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0)
known_button.grid(row=0, column=2)

window.mainloop()
