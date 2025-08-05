import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = length_var.get()
    if length < 4:
        messagebox.showwarning("Invalid", "Password length should be at least 4")
        return

    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Empty", "No password to copy")

# ===== GUI Setup =====
root = tk.Tk()
root.title("Password Generator")
root.geometry("350x250")
root.configure(bg="#f0faff")

# Heading
tk.Label(root, text="🔐 Password Generator", font=("Helvetica", 16, "bold"), bg="#f0faff", fg="#0d47a1").pack(pady=10)

# Password Length
length_var = tk.IntVar(value=12)
tk.Label(root, text="Password Length:", bg="#f0faff", font=("Arial", 12)).pack()
tk.Spinbox(root, from_=4, to=32, textvariable=length_var, font=("Arial", 12), width=5).pack(pady=5)

# Password Entry
password_entry = tk.Entry(root, font=("Arial", 14), width=25)
password_entry.pack(pady=10)

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password, bg="#4CAF50", fg="white", font=("Arial", 11)).pack(pady=5)

# Copy Button
tk.Button(root, text="Copy Password", command=copy_password, bg="#2196F3", fg="white", font=("Arial", 11)).pack(pady=5)

root.mainloop()