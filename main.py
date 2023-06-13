from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    password_entry.delete(0, END)
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '(', ')', '&', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_save = website.get()
    email_save = email.get()
    password_save = password_entry.get()

    if len(website_save) == 0 or len(password_save) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields")
    else:
        is_ok = messagebox.askokcancel(title=website_save, message=f"These are the details entered: \nEmail: {email_save} \nPassword: {password_save} \nIs it  ok to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website_save} | {email_save} | {password_save}\n")
                website.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


canvas = Canvas(width=200, height=200, highlightthickness=0)
pass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=pass_img)
canvas.grid(column=1, row=0)

website_l = Label(text="Website:")
website_l.grid(column=0, row=1)

website = Entry(width=51)
website.grid(column=1, row=1, columnspan=2)
website.focus()


email_username_l = Label(text="Email/Username:")
email_username_l.grid(column=0, row=2)

email = Entry(width=51)
email.insert(0, "huzefa.ahmed.web@gmail.com")
email.grid(column=1, row=2, columnspan=2)

password_l = Label(text="Password:")
password_l.grid(column=0, row=3)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=43, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()
