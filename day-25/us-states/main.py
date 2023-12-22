import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
correct_list = []
learn_list = []

typer = turtle.Turtle()
typer.hideturtle()
typer.penup()

while len(correct_list) < 50:
    answer_state = screen.textinput(title=f"{len(correct_list)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        learn_list = [state for state in state_list if state not in correct_list]

        learn_data = pandas.DataFrame(learn_list)
        learn_data.to_csv("states_to_learn.csv")
        break

    elif answer_state in state_list:
        correct_list.append(answer_state)
        answer_data = data[data.state == answer_state]
        typer.goto(answer_data.x.iloc[0], answer_data.y.iloc[0])
        typer.write(answer_state)



# state_data = data[data.state == guess_state.capitalize()]
# if len(state_data) > 0:
#     x_cor = state_data.x.to_list()[0]
#     y_cor = state_data.y.to_list()[0]
#     name = state_data.state.to_list()[0]
#     typer.goto(x_cor, y_cor)
#     typer.write(name)



turtle.mainloop()
