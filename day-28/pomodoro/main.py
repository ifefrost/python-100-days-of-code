import tkinter.messagebox
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
timer = None
reps = 0
content = ''

# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    global reps, content

    start_btn.config(state="normal")
    reset_btn.config(state="disabled")

    window.after_cancel(timer)
    title_lbl.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0
    content = ''
    check_lbl.config(text=content)

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    reps += 1

    start_btn.config(state="disabled")
    reset_btn.config(state="normal")

    if reps % 8 == 0:
        tkinter.messagebox.showinfo(title="Break", message="Take a Long 20 minute Break!")
        title_lbl.config(text="Break", fg=RED)
        countdown(long_break_sec)
    elif reps % 2 == 0:
        tkinter.messagebox.showinfo(title="Break", message="Take a short 5 minute Break!")
        title_lbl.config(text="Break", fg=PINK)
        countdown(short_break_sec)
    else:
        tkinter.messagebox.showinfo(title="Work", message="Work for 25 minutes")
        title_lbl.config(text="Work", fg=GREEN)
        countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    count_min = count // 60
    count_sec = count % 60
    global content
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        window.lift()
        window.attributes('-topmost', True)
        window.after_idle(window.attributes, '-topmost', False)
        start_timer()
        if reps % 2 == 0:
            content += "✅"
            check_lbl.config(text=content)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# tomato image canvas with timer
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 25, "bold"))

# text components
title_lbl = Label(text="Timer", font=(FONT_NAME, 45), fg=GREEN, bg=YELLOW)
check_lbl = Label(font=(FONT_NAME, 15), fg=GREEN, bg=YELLOW)

# buttons
start_btn = Button(text="Start", borderwidth=0, highlightthickness=0,
                   bg="white", padx=10, pady=5, command=start_timer)
reset_btn = Button(text="Reset", highlightthickness=0, borderwidth=0,
                   bg="white", padx=10, pady=5, command=reset_timer, state="disabled")

title_lbl.grid(column=1, row=0)
check_lbl.grid(column=1, row=3)
canvas.grid(column=1, row=1)
start_btn.grid(column=0, row=2)
reset_btn.grid(column=2, row=2)
window.mainloop()
