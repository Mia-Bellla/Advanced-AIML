import tkinter as tk

# Window setup
root = tk.Tk()
root.title("Tkinter Example")
root.geometry("400x250")
root.configure(bg="#f9f5f0")  # soft background color

# Title label
title = tk.Label(
    root,
    text="Welcome, User",
    font=("Helvetica", 20, "bold"),
    fg="#3a3a3a",
    bg="#f9f5f0"
)
title.pack(pady=20)

# Entry widget with rounded-ish effect
entry = tk.Entry(
    root,
    font=("Helvetica", 14),
    width=25,
    bd=2,
    relief="groove"
)
entry.pack(pady=10)

# Dynamic label
output = tk.Label(
    root,
    text="Type something above 👆",
    font=("Helvetica", 12),
    fg="#555",
    bg="#f9f5f0"
)
output.pack(pady=10)

# Button functions
def show_text():
    user_text = entry.get()
    if user_text.strip() == "":
        output.config(text="You didn’t type anything!")
    else:
        output.config(text=f"You typed: {user_text}")

# Aesthetic button
button = tk.Button(
    root,
    text="Show Text",
    font=("Helvetica", 12, "bold"),
    fg="black",
    bg="#6c63ff",
    activebackground="#574fd6",
    activeforeground="white",
    padx=15,
    pady=5,
    relief="flat",
    command=show_text
)
button.pack(pady=15)

root.mainloop()
