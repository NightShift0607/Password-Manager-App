from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import json


# Random Password Generator

def random_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 
            'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)
    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]
    rand_password = password_letter + password_number + password_symbol
    random.shuffle(rand_password)
    rand_password = ''.join(rand_password)
    password.insert(0, rand_password)


# Saving Password

def chk_password():
    name = website_name.get()
    pas = password.get()
    
    if len(name) == 0 or len(pas) == 0:
        messagebox.showinfo(title="Error", message="Please make sure you have filled all the fields")
    else :
        save_password()

def save_password():
    name = website_name.get()
    user = user_name.get()
    pas = password.get()
    
    is_ok = messagebox.askokcancel(title=name, message=f"These are the details entered: \nUsername: {user} \nPassword: {pas} \nIs it ok to save?")
    
    new_data = {
        name: {
            "Username": user,
            "Password" : pas
        }
    }
    
    if is_ok:
        try:
            with open("SavedPasswords.json","r") as data_file:
                old_data = json.load(data_file)
                old_data.update(new_data)   
        except FileNotFoundError:
            with open("SavedPasswords.json","w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("SavedPasswords.json","w") as data_file:
                json.dump(old_data, data_file, indent=4)
        finally:
            website_name.delete(0, END)
            user_name.delete(0, END)
            user_name.insert(0, "NightShift0607")
            password.delete(0,END)

#  Searching Password

def search_website():
    with open("SavedPasswords.json","r") as file:
        data = json.load(file)
    website = website_name.get()
    
    try:
        result = data[website]
    except KeyError:
        messagebox.showinfo(title="Not Found", message="The website name you entered is not present.\nPlease make sure you have spelled it right")
    else:
        messagebox.showinfo(title=website, message=f"Username: {result["Username"]} \nPassword: {result["Password"]}")

# UI Setup

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
image = Image.open("icon.png")
image = image.resize((200,200))
icon = ImageTk.PhotoImage(image)
canvas.create_image(100, 100, image=icon)
canvas.grid(row=0, column=1)
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_name = Entry(width=27)
website_name.focus()
website_name.grid(row=1, column=1)
search_pass_btn = Button(text="Search Website", command=search_website, width=14)
search_pass_btn.grid(row=1, column=2)
user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)
user_name = Entry(width=45)
user_name.insert(END, "NightShift0607")
user_name.grid(row=2, column=1, columnspan=2)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password = Entry(width=27)
password.grid(row=3, column=1)
generate_pass_btn = Button(text="Generate Password", command=random_password)
generate_pass_btn.grid(row=3, column=2)
add_btn = Button(text="Add",width=40,command=chk_password)
add_btn.grid(row=4, column=1, columnspan=2)




window.mainloop()