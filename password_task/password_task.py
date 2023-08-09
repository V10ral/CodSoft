import tkinter as tk
from tkinter import messagebox
import random
import string
    
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
        password_chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(password_chars) for _ in range(length))
        password_display.config(text=f"Generated Password: {password}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer for password length.")

# Create the main application window
app = tk.Tk()
app.title("Password Generator by viral parmar")
app.geometry("400x200")

# Create GUI elements
length_label = tk.Label(app,fg='white',bg='black', text="Enter password length:")
length_label.pack(pady=10)

length_entry = tk.Entry(app)
length_entry.pack(pady=5)

generate_button = tk.Button(app,fg='white',bg='black', text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_display = tk.Label(app,fg='black', text="Generated Password: ")
password_display.pack(pady=5)

app.mainloop()