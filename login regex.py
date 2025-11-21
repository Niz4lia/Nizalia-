import tkinter as tk
from tkinter import messagebox
import re
def log():
    user=r"Nizalia"
    passw=r"1234"
    
    username = username_entry.get()
    password = password_entry.get()
    
    if re.fullmatch(user, username) and re.fullmatch(passw, password):
        messagebox.showinfo("Login", "Login successful")
    else:
        messagebox.showerror("Login", "Invalid Username or Password")
root = tk.Tk()
root.title("Login System")
root.geometry("450x250")
root.config(bg="#96bfd6")

tk.Label(root, text="Username:").pack(pady=5)
username_entry = tk.Entry(root)

username_entry.pack(pady=5)

tk.Label(root, text="Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Login", command=log).pack(pady=10)

root.mainloop()
