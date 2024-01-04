from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for char in range(randint(2, 4))]
    password_list += [choice(numbers) for char in range(randint(2, 4))]

    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(END, password)
    pyperclip.copy(password)
# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data:
            file = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found!")
    else:
        if website in file:
            details = file[website]
            messagebox.showinfo(title=website, message=f"Email: {details["email"]}\nPassword: {details["password"]}")
        else:
            messagebox.showinfo(title="Oops", message="No details for the website exists!")
       

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(password) == 0 or len(website) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="You left some fields empty!")
    else:
        try:
            with open("data.json", "r") as data:
                file = json.load(data)
        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)
        else:
            file.update(new_data)
            with open("data.json", "w") as data:
                json.dump(file, data, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_lbl = Label(text="Website:", bg="white", pady=3)
email_lbl = Label(text="Email/Username:", bg="white", pady=3)
password_lbl = Label(text="Password:", bg="white", pady=3)

website_entry = Entry(window, width=35, highlightthickness=1,
                      highlightcolor="#77c3ec")
email_entry = Entry(window, width=35, highlightthickness=1,
                    highlightcolor="#77c3ec")
password_entry = Entry(window, width=30, highlightthickness=1,
                       highlightcolor="#77c3ec")

gen_password_btn = Button(text="Generate Password", command=generate_password)
add_btn = Button(text="Add", width=45, command=save)
search_btn = Button(text="Search", width=15, command=find_password)

website_lbl.grid(column=0, row=1)
website_entry.grid(column=1, row=1)
website_entry.focus()
email_lbl.grid(column=0, row=2)
email_entry.grid(column=1, row=2, columnspan=2, sticky=EW)
email_entry.insert(END, "user@email.com")
password_lbl.grid(column=0, row=3)
password_entry.grid(column=1, row=3, sticky=EW)
gen_password_btn.grid(column=2, row=3)
add_btn.grid(column=1, row=4, columnspan=2)
search_btn.grid(column=2, row=1)

window.mainloop()
