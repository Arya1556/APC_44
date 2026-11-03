
#STUDENT REGISTRATION FORM
import tkinter as tk
from tkinter import messagebox

# Create window
root = tk.Tk()
root.title("Student Registration Form")
root.geometry("350x400")

# Heading
tk.Label(root, text="Student Registration Form",
         font=("Arial", 16, "bold")).pack(pady=15)

# Student Name
tk.Label(root, text="Student Name").pack()
name = tk.Entry(root)
name.pack(pady=5)

# Roll Number
tk.Label(root, text="Roll Number").pack()
roll = tk.Entry(root)
roll.pack(pady=5)

# Email
tk.Label(root, text="Email").pack()
email = tk.Entry(root)
email.pack(pady=5)

# Course
tk.Label(root, text="Course").pack()
course = tk.Entry(root)
course.pack(pady=5)

# Submit button function
def register():
    n = name.get()
    r = roll.get()
    e = email.get()
    c = course.get()

    if n == "" or r == "" or e == "" or c == "":
        messagebox.showerror("Error", "Please fill all fields")
    else:
        messagebox.showinfo(
            "Success",
            "Registration Successful!\n"
            + "Name: " + n + "\n"
            + "Roll Number: " + r + "\n"
            + "Email: " + e + "\n"
            + "Course: " + c
        )

# Register button
tk.Button(root, text="Register",
          command=register,
          bg="green", fg="white").pack(pady=20)

# Run window
root.mainloop()

#VALIDATION FORM
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Registration Form")
root.geometry("300x300")

tk.Label(root, text="Student Registration",
         font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Name").pack()
name = tk.Entry(root)
name.pack()

tk.Label(root, text="Age").pack()
age = tk.Entry(root)
age.pack()

tk.Label(root, text="Email").pack()
email = tk.Entry(root)
email.pack()

def register():
    n = name.get().strip()
    a = age.get().strip()
    e = email.get().strip()

    if n == "" or a == "" or e == "":
        messagebox.showerror("Error", "Fill all fields")
    elif not n.replace(" ", "").isalpha():
        messagebox.showerror("Error", "Enter a valid name")
    elif not a.isdigit() or int(a) < 1 or int(a) > 120:
        messagebox.showerror("Error", "Enter a valid age")
    elif "@" not in e or "." not in e:
        messagebox.showerror("Error", "Enter a valid email")
    else:
        messagebox.showinfo("Success", "Registration Successful!")

tk.Button(root, text="Register",
          command=register).pack(pady=15)

root.mainloop()


#NOTEPAD 

import tkinter as tk
from tkinter import filedialog, messagebox

# Create window
root = tk.Tk()
root.title("Untitled - Notepad")
root.geometry("600x400")

# Create text area
text_area = tk.Text(root, font=("Arial", 12), undo=True)
text_area.pack(fill="both", expand=True)

# New file
def new_file():
    text_area.delete("1.0", tk.END)
    root.title("Untitled - Notepad")

# Open file
def open_file():
    file = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file:
        with open(file, "r", encoding="utf-8") as f:
            text_area.delete("1.0", tk.END)
            text_area.insert("1.0", f.read())
        root.title(file + " - Notepad")

# Save file
def save_file():
    file = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file:
        with open(file, "w", encoding="utf-8") as f:
            f.write(text_area.get("1.0", tk.END))
        root.title(file + " - Notepad")
        messagebox.showinfo("Notepad", "File saved successfully!")

# Create menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Run application
root.mainloop()
