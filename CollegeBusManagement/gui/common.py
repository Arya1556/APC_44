import tkinter as tk
from tkinter import messagebox, ttk


def show_error(error: Exception) -> None:
    messagebox.showerror("Operation failed", str(error))


def selected_id(tree: ttk.Treeview) -> int | None:
    selection = tree.selection()
    if not selection:
        return None
    return int(tree.item(selection[0], "values")[0])


def make_tree(parent, columns: tuple[str, ...], headings: tuple[str, ...]) -> ttk.Treeview:
    tree = ttk.Treeview(parent, columns=columns, show="headings", height=12)
    for column, heading in zip(columns, headings):
        tree.heading(column, text=heading)
        tree.column(column, width=125, anchor=tk.W)
    tree.pack(fill=tk.BOTH, expand=True, padx=8, pady=6)
    return tree


def replace_tree(tree: ttk.Treeview, rows) -> None:
    tree.delete(*tree.get_children())
    for row in rows:
        tree.insert("", tk.END, values=tuple(row))
