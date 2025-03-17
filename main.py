from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("data.txt", "a") as f:

        website = website_input.get()
        email = email_user_input.get()
        password =  password_input.get()
        f.write(f"{website}     |       {email}     |       {password}\n")
    website_input.delete(0, "end")
    email_user_input.delete(0, "end")
    email_user_input.insert(0, "tuan1214502@gmail.com")
    password_input.delete(0, "end")
    website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0,column=1)

# Website
website_text = Label(text="Website")
website_text.grid(row=1, column=0)
website_input = Entry()
website_input.focus()
website_input.grid(row=1,column=1,columnspan=2,sticky="EW")

# Email/Username
email_user_text = Label(text="Email/Username:")
email_user_text.grid(row=2, column=0)

email_user_input = Entry()
email_user_input.grid(row=2,column=1,columnspan=2,sticky="EW")
email_user_input.insert(0, "tuan1214502@gmail.com")

# Password
password_text = Label(text="Password:")
password_text.grid(row=3, column=0)

password_input = Entry()
password_input.grid(row=3,column=1,sticky="EW")

# Generate button
generate_btn = Button(text="Generate Password")
generate_btn.grid(row=3,column=2)

# Add button
add_btn = Button(text="Add", width=35, command=save)
add_btn.grid(row=4, column=1,columnspan=2,sticky="EW")



window.mainloop()