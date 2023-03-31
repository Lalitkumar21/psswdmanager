import tkinter as tk
from io import BytesIO
from urllib.request import urlopen
from PIL import ImageTk, Image
import random
import string

mw = tk.Tk()
mw.title("Password Manager")
mw.geometry("600x350")

# importing image in tkinter
def importimg():
    url = "https://static.techspot.com/images2/news/bigimage/2020/01/2020-01-24-image-20.jpg"
    with urlopen(url) as u:
        raw_data = u.read()

    img = Image.open(BytesIO(raw_data))
    img.thumbnail((300, 300))
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(mw, image=photo)
    label.image = photo  # keep a reference to the image to prevent garbage collection
    label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    label.grid_configure(padx=10, pady=10, sticky="nsew")
    mw.grid_rowconfigure(0, weight=1)
    mw.grid_columnconfigure(0, weight=1)

importimg()

tk.Label(mw, text="Enter String:").grid(row=1, column=0, padx=10, pady=10)
password_var = tk.StringVar()
tk.Entry(mw, textvariable=password_var).grid(row=1, column=1, padx=10, pady=10)

password_label = tk.Label(mw, text="", font=("Helvetica", 14))
password_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

def checkpsswd():
    password = password_var.get()
    
    # Checking length of password
    length = len(password)
    if length < 8:
        password_label.configure(text="Password is too short")
        return
    
    # Checking for uppercase letters, lowercase letters, digits, and special characters
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False
    
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_special = True
    
    if not (has_uppercase and has_lowercase and has_digit and has_special):
        password_label.configure(text="Password is weak (missing required characters)")
        return
    
    # Checking for common words and patterns
    common_patterns = ['password', '123', 'qwerty', 'abc', 'admin']
    for pattern in common_patterns:
        if pattern in password.lower():
            password_label.configure(text="Password is weak (contains common word/pattern)")
            return
    
    password_label.configure(text="Password is strong!")


checkpsswd()
# To generate strong password
# To generate strong password
def generatestrongpassword():
    length = 12
    while True:
        uppercase_letters = random.choices(string.ascii_uppercase, k=1)
        lowercase_letters = random.choices(string.ascii_lowercase, k=1)
        digits = random.choices(string.digits, k=1)
        special_characters = random.choices(string.punctuation, k=1)
        password = ''.join(uppercase_letters + lowercase_letters + digits + special_characters)
        password += ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length-4))
        password_list = list(password)
        random.shuffle(password_list)
        password = ''.join(password_list)
        if (any(char.isupper() for char in password)
                and any(char.islower() for char in password)
                and any(char.isdigit() for char in password)
                and any(char in string.punctuation for char in password)):
            break

    password_var.set(password)
    password_label.configure(text="Generated Password: " + password)


tk.Button(mw, text="Generate Password", command=generatestrongpassword).grid(row=3, column=0, columnspan=2, padx=10, pady=10)
tk.Button(mw, text="Check Password", command=checkpsswd).grid(row=3, column=3, columnspan=1, padx=10, pady=10)
mw.mainloop()
