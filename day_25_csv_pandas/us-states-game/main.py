import turtle
import pandas
from text_mover import TextMover


screen = turtle.Screen()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
text = TextMover()
data = pandas.read_csv('50_states.csv')

round_count = 0

while round_count != 50:
    guess_state = screen.textinput(title='Guess a State', prompt='Enter a state name you know').title()
    state = data[data['state'] == guess_state]
    # text.write_state(state.state.to_string(), state.x, state.y)
    print(state.x)
turtle.mainloop()
