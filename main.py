from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))

    rand_letter = [choice(letters) for _ in range(randint(8, 10))]
    rand_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    rand_number = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = rand_letter + rand_number + rand_symbol

    shuffle(password_list)

    password_gen = "".join(password_list)

    password_input.delete(0, "end")
    password_input.insert(0, password_gen)
    pyperclip.copy(password_gen)
    print(f"Your password is: {password_gen}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_user_input.get()
    password = password_input.get()
    new_data = {website: {
        "email": email,
        "password": password

    }}

    if len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, "end")
            email_user_input.delete(0, "end")
            email_user_input.insert(0, "tuan1214502@gmail.com")
            password_input.delete(0, "end")
            website_input.focus()

# Search account
def find_password():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError as error_message:
        messagebox.showerror(title="Error", message="File Not Found")
    else:
        try:
            search_object = website_input.get()
            print(data.get(search_object))
            seach_result = data.get(search_object)
            messagebox.showinfo(title=search_object, message=f"Email: {seach_result.get("email")} \n Password: {seach_result.get("password")}")
        except AttributeError:
            messagebox.showerror(title="Error", message=f"No details fo the {search_object} exists")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# Website
website_text = Label(text="Website")
website_text.grid(row=1, column=0)
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1)

# Search button
search_button = Button(text="Search", command=find_password, width=14)
search_button.grid(row=1, column=2)
# Email/Username
email_user_text = Label(text="Email/Username:")
email_user_text.grid(row=2, column=0)

email_user_input = Entry()
email_user_input.grid(row=2, column=1, columnspan=2, sticky="EW")
email_user_input.insert(0, "tuan1214502@gmail.com")

# Password
password_text = Label(text="Password:")
password_text.grid(row=3, column=0)

password_input = Entry()
password_input.grid(row=3, column=1, sticky="EW")

# Generate button
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(row=3, column=2)

# Add button
add_btn = Button(text="Add", width=35, command=save)
add_btn.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
