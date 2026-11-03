import tkinter as tk
from tkinter import messagebox, ttk
from typing import Callable

from CollegeBusManagement.modules.authentication import (
    MIN_PASSWORD_LENGTH,
    admin_exists,
    authenticate_admin,
    create_admin,
)


class LoginWindow:
    def __init__(self, root: tk.Tk, on_authenticated: Callable[[str], None]):
        self.root = root
        self.on_authenticated = on_authenticated
        self.creating_first_admin = not admin_exists()
        root.title("College Bus Management System - Admin Login")
        root.geometry("470x360" if self.creating_first_admin else "470x300")
        root.resizable(False, False)

        self.frame = ttk.Frame(root, padding=28)
        self.frame.pack(fill=tk.BOTH, expand=True)
        ttk.Label(
            self.frame,
            text="College Bus Management System",
            font=("Segoe UI", 17, "bold"),
        ).pack(pady=(6, 12))
        heading = "Create the first administrator account" if self.creating_first_admin else "Admin Login"
        ttk.Label(self.frame, text=heading).pack(pady=(0, 10))

        fields = ttk.Frame(self.frame)
        fields.pack(fill=tk.X)
        ttk.Label(fields, text="Admin Username").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.username = ttk.Entry(fields, width=34)
        self.username.grid(row=0, column=1, sticky=tk.EW, padx=(12, 0), pady=5)
        ttk.Label(fields, text="Password").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.password = ttk.Entry(fields, width=34, show="*")
        self.password.grid(row=1, column=1, sticky=tk.EW, padx=(12, 0), pady=5)
        self.confirm_password = None
        if self.creating_first_admin:
            ttk.Label(fields, text="Confirm Password").grid(row=2, column=0, sticky=tk.W, pady=5)
            self.confirm_password = ttk.Entry(fields, width=34, show="*")
            self.confirm_password.grid(row=2, column=1, sticky=tk.EW, padx=(12, 0), pady=5)
            ttk.Label(
                self.frame,
                text=f"Choose a password with at least {MIN_PASSWORD_LENGTH} characters.",
                wraplength=390,
            ).pack(anchor=tk.W, pady=(6, 0))
        fields.columnconfigure(1, weight=1)

        actions = ttk.Frame(self.frame)
        actions.pack(pady=16)
        action_label = "Create Admin Account" if self.creating_first_admin else "Login"
        ttk.Button(actions, text=action_label, command=self.submit).pack(side=tk.LEFT, padx=5)
        ttk.Button(actions, text="Clear", command=self.clear).pack(side=tk.LEFT, padx=5)
        self.root.bind("<Return>", lambda _event: self.submit())
        self.username.focus_set()

    def submit(self) -> None:
        username = self.username.get().strip()
        password = self.password.get()
        if self.creating_first_admin:
            confirmation = self.confirm_password.get() if self.confirm_password else ""
            if password != confirmation:
                messagebox.showerror("Password mismatch", "The passwords do not match.", parent=self.root)
                return
            try:
                create_admin(username, password)
            except Exception as error:
                messagebox.showerror("Account setup failed", str(error), parent=self.root)
                return
            messagebox.showinfo(
                "Administrator created",
                "Your admin account is ready. Log in with the username and password you just created.",
                parent=self.root,
            )
            self.frame.destroy()
            self.__init__(self.root, self.on_authenticated)
            return

        try:
            authenticated = authenticate_admin(username, password)
        except Exception as error:
            messagebox.showerror(
                "Login unavailable", f"Could not verify the admin account: {error}", parent=self.root
            )
            return
        if not authenticated:
            messagebox.showerror(
                "Login failed", "Incorrect admin username or password.", parent=self.root
            )
            self.password.delete(0, tk.END)
            self.password.focus_set()
            return
        self.password.delete(0, tk.END)
        self.username.delete(0, tk.END)
        self.on_authenticated(username)

    def clear(self) -> None:
        self.username.delete(0, tk.END)
        self.password.delete(0, tk.END)
        if self.confirm_password is not None:
            self.confirm_password.delete(0, tk.END)
        self.username.focus_set()
