import tkinter as tk
from tkinter import messagebox, ttk

from CollegeBusManagement.gui.common import make_tree, selected_id, show_error
from CollegeBusManagement.models.fee import Fee
from CollegeBusManagement.modules import fee_management, student_management


class FeeWindow(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=8)
        form = ttk.LabelFrame(self, text="Transport fee payment", padding=8)
        form.pack(fill=tk.X)
        ttk.Label(form, text="Student").grid(row=0, column=0, sticky=tk.W)
        self.student = ttk.Combobox(form, width=38, state="readonly")
        self.student.grid(row=1, column=0, padx=4)
        self.total = self._entry(form, "Total fee", 1)
        self.paid = self._entry(form, "Amount paid", 2)
        self.date = self._entry(form, "Payment date (YYYY-MM-DD)", 3)
        self.date.insert(0, "")
        actions = ttk.Frame(self)
        actions.pack(fill=tk.X, pady=5)
        for label, command in (("Record payment", self.add), ("Update selected", self.update),
                               ("Delete selected", self.delete), ("Clear", self.clear)):
            ttk.Button(actions, text=label, command=command).pack(side=tk.LEFT, padx=3)
        self.tree = make_tree(
            self, ("id", "student", "roll", "total", "paid", "balance", "status", "date"),
            ("ID", "Student", "Roll", "Total", "Paid", "Outstanding", "Status", "Date"),
        )
        self.tree.bind("<<TreeviewSelect>>", self._select)
        self.refresh()

    @staticmethod
    def _entry(parent, label, column):
        ttk.Label(parent, text=label).grid(row=0, column=column, sticky=tk.W)
        entry = ttk.Entry(parent, width=23)
        entry.grid(row=1, column=column, padx=4)
        return entry

    def refresh(self):
        self.students = student_management.list_students()
        self.student_values = [f"{row['id']} | {row['roll_number']} | {row['name']}" for row in self.students]
        self.student["values"] = self.student_values
        self.tree.delete(*self.tree.get_children())
        for row in fee_management.list_fees():
            self.tree.insert("", tk.END, values=(
                row["id"], row["name"], row["roll_number"], row["total_fee"],
                row["amount_paid"], row["outstanding"], row["status"], row["payment_date"],
            ))

    def _fee(self):
        try:
            student_id = int(self.student.get().split(" | ", 1)[0])
        except (ValueError, IndexError):
            raise ValueError("Select a student.")
        return Fee(
            student_id=student_id,
            total_fee=float(self.total.get()),
            amount_paid=float(self.paid.get() or 0),
            payment_date=self.date.get().strip() or None,
        )

    def add(self):
        try:
            fee_management.add_fee(self._fee())
            self.refresh()
        except Exception as error:
            show_error(error)

    def update(self):
        fee_id = selected_id(self.tree)
        if fee_id is None:
            messagebox.showinfo("Select a fee", "Select a payment record first.")
            return
        try:
            fee_management.update_fee(fee_id, self._fee())
            self.refresh()
        except Exception as error:
            show_error(error)

    def delete(self):
        fee_id = selected_id(self.tree)
        if fee_id is None:
            messagebox.showinfo("Select a fee", "Select a payment record first.")
            return
        if messagebox.askyesno("Confirm deletion", "Delete the selected fee record?"):
            try:
                fee_management.delete_fee(fee_id)
                self.refresh()
            except Exception as error:
                show_error(error)

    def _select(self, _event):
        values = self.tree.item(self.tree.selection()[0], "values")
        self.student.set(next((value for value in self.student_values
                               if value.startswith(f"{self._student_id(values[2])} |")), ""))
        self.total.delete(0, tk.END)
        self.total.insert(0, values[3])
        self.paid.delete(0, tk.END)
        self.paid.insert(0, values[4])
        self.date.delete(0, tk.END)
        self.date.insert(0, values[7])

    def _student_id(self, roll):
        return next((row["id"] for row in self.students if row["roll_number"] == roll), -1)

    def clear(self):
        self.student.set("")
        for entry in (self.total, self.paid, self.date):
            entry.delete(0, tk.END)
