from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
flip = None
word = None

# ---------- READ DATA FROM CSV ----------
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/frequent_french.csv")

words_dict = {row.French: row.English for (index, row) in data.iterrows()}
word_list = data.French.to_list()


def new_word():
    global flip, word
    try:
        window.after_cancel(flip)
    except ValueError:
        pass
    finally:
        word = choice(word_list)
        canvas.itemconfig(canvas_image, image=card_image)
        canvas.itemconfig(title_text, text="French")
        canvas.itemconfig(word_text, text=word)
        flip = window.after(3000, flip_card, word)


def correct():
    global word
    word_list.remove(word)

    new_words_dict = {w: words_dict[w] for w in word_list}
    words_to_learn = pandas.DataFrame(new_words_dict.items(), columns=['French', 'English'])
    words_to_learn.to_csv("data/words_to_learn.csv", index=False)

    new_word()


# --------------- FLIP CARD --------------
def flip_card(word):
    canvas.itemconfig(canvas_image, image=back_card_image)
    canvas.itemconfig(title_text, text="English")
    canvas.itemconfig(word_text, text=words_dict[word])


# -------------- UI SETUP -----------------
window = Tk()
window.title("Learn French Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = PhotoImage(file="images/card_front.png")
back_card_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_image)


title_text = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

wrong_image = PhotoImage(file="images/wrong.png")
right_image = PhotoImage(file="images/right.png")

wrong_btn = Button(image=wrong_image, bd=0, highlightthickness=0, command=new_word)
right_btn = Button(image=right_image, bd=0, highlightthickness=0, command=correct)

canvas.grid(column=0, row=0, columnspan=2)
wrong_btn.grid(column=0, row=1)
right_btn.grid(column=1, row=1)

new_word()


window.mainloop()
