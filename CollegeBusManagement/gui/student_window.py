import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from CollegeBusManagement.gui.common import make_tree, selected_id, show_error
from CollegeBusManagement.models.student import Student
from CollegeBusManagement.modules import route_management, student_management
from CollegeBusManagement.modules.bus_management import list_buses
from CollegeBusManagement.utils.file_handler import import_students


class StudentWindow(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=8)
        self.student_id = None
        self.current_bus_id = None
        self.current_seat_number = None
        self.manual_seat_authorized = False
        self.fields = {}
        self._form()
        self.tree = make_tree(
            self, ("id", "name", "roll", "department", "year", "contact", "bus", "route", "stop", "seat"),
            ("ID", "Name", "Roll", "Department", "Year", "Contact", "Bus", "Route", "Pickup", "Seat"),
        )
        self.tree.bind("<<TreeviewSelect>>", self._select)
        self.refresh()

    def _form(self):
        form = ttk.LabelFrame(self, text="Student details", padding=8)
        form.pack(fill=tk.X)
        specs = (("Name", "name"), ("Roll number", "roll"), ("Department", "department"),
                 ("Year", "year"), ("Contact", "contact"), ("Seat (blank = auto)", "seat"))
        for index, (label, key) in enumerate(specs):
            ttk.Label(form, text=label).grid(row=index // 3 * 2, column=index % 3 * 2, sticky=tk.W)
            entry = ttk.Entry(form, width=22)
            entry.grid(row=index // 3 * 2 + 1, column=index % 3 * 2, padx=4, pady=3)
            self.fields[key] = entry
            if key == "seat":
                entry.configure(state="readonly")
        ttk.Label(form, text="Bus").grid(row=0, column=6, sticky=tk.W)
        self.bus = ttk.Combobox(form, width=24, state="readonly")
        self.bus.grid(row=1, column=6, padx=4)
        ttk.Label(form, text="Route").grid(row=2, column=6, sticky=tk.W)
        self.route = ttk.Combobox(form, width=24, state="readonly")
        self.route.grid(row=3, column=6, padx=4)
        ttk.Label(form, text="Pickup stop").grid(row=4, column=6, sticky=tk.W)
        self.stop = ttk.Combobox(form, width=24, state="readonly")
        self.stop.grid(row=5, column=6, padx=4)
        self.route.bind("<<ComboboxSelected>>", lambda _event: self._load_stops())
        actions = ttk.Frame(self)
        actions.pack(fill=tk.X, pady=4)
        ttk.Button(actions, text="Add", command=self.add).pack(side=tk.LEFT, padx=3)
        ttk.Button(actions, text="Update selected", command=self.update).pack(side=tk.LEFT, padx=3)
        ttk.Button(actions, text="Delete selected", command=self.delete).pack(side=tk.LEFT, padx=3)
        ttk.Button(actions, text="Clear", command=self.clear).pack(side=tk.LEFT, padx=3)
        ttk.Button(actions, text="Authorize manual seats", command=self.authorize_manual_seats).pack(
            side=tk.LEFT, padx=3
        )
        ttk.Label(actions, text="Search").pack(side=tk.LEFT, padx=(20, 4))
        self.search = ttk.Entry(actions, width=25)
        self.search.pack(side=tk.LEFT)
        ttk.Button(actions, text="Find", command=self.refresh).pack(side=tk.LEFT, padx=3)
        ttk.Button(actions, text="Import CSV", command=self.import_csv).pack(side=tk.LEFT, padx=3)
        self.refresh_choices()

    def refresh_choices(self):
        self.bus_rows = list_buses()
        self.route_rows = route_management.list_routes()
        self.bus_values = [f"{row['id']} | {row['bus_number']}" for row in self.bus_rows]
        self.route_values = [f"{row['id']} | {row['route_name']}" for row in self.route_rows]
        self.bus["values"] = self.bus_values
        self.route["values"] = self.route_values
        self._load_stops()

    def _load_stops(self):
        route_id = self._combo_id(self.route.get())
        self.stop_rows = route_management.list_stops(route_id) if route_id else []
        self.stop_values = [f"{row['id']} | {row['stop_name']}" for row in self.stop_rows]
        self.stop["values"] = self.stop_values
        if self.stop.get() not in self.stop_values:
            self.stop.set("")

    @staticmethod
    def _combo_id(value):
        try:
            return int(value.split(" | ", 1)[0])
        except (ValueError, IndexError):
            return None

    def _student(self):
        if self.manual_seat_authorized:
            seat_number = int(self.fields["seat"].get()) if self.fields["seat"].get().strip() else None
        elif self.student_id is not None and self._combo_id(self.bus.get()) == self.current_bus_id:
            seat_number = self.current_seat_number
        else:
            seat_number = None
        return Student(
            name=self.fields["name"].get(), roll_number=self.fields["roll"].get(),
            department=self.fields["department"].get(), year=self.fields["year"].get(),
            contact_number=self.fields["contact"].get(), bus_id=self._combo_id(self.bus.get()),
            route_id=self._combo_id(self.route.get()), pickup_stop_id=self._combo_id(self.stop.get()),
            seat_number=seat_number,
        )

    def _set_seat_value(self, value):
        seat_entry = self.fields["seat"]
        seat_entry.configure(state="normal")
        seat_entry.delete(0, tk.END)
        if value:
            seat_entry.insert(0, value)
        if not self.manual_seat_authorized:
            seat_entry.configure(state="readonly")

    def authorize_manual_seats(self):
        self.manual_seat_authorized = True
        self.fields["seat"].configure(state="normal")
        messagebox.showinfo(
            "Admin authorization",
            "Manual seat assignment is enabled for this authenticated admin session.",
        )

    def add(self):
        try:
            student_management.add_student(self._student())
            self.clear()
            self.refresh()
        except Exception as error:
            show_error(error)

    def update(self):
        if self.student_id is None:
            messagebox.showinfo("Select a student", "Select a student record first.")
            return
        try:
            student_management.update_student(self.student_id, self._student())
            self.refresh()
        except Exception as error:
            show_error(error)

    def delete(self):
        student_id = selected_id(self.tree)
        if student_id is None:
            messagebox.showinfo("Select a student", "Select a student record first.")
            return
        if messagebox.askyesno("Confirm deletion", "Delete the selected student and fee records?"):
            try:
                student_management.delete_student(student_id)
                self.clear()
                self.refresh()
            except Exception as error:
                show_error(error)

    def clear(self):
        self.student_id = None
        self.current_bus_id = None
        self.current_seat_number = None
        for key, field in self.fields.items():
            if key == "seat":
                continue
            field.delete(0, tk.END)
        self._set_seat_value("")
        self.bus.set("")
        self.route.set("")
        self.stop.set("")

    def _select(self, _event):
        selection = self.tree.selection()
        if not selection:
            return
        values = self.tree.item(selection[0], "values")
        self.student_id = int(values[0])
        self.current_bus_id = self._combo_id(
            next((item for item in self.bus_values if item.startswith(f"{values[6]} |")), "")
        )
        self.current_seat_number = int(values[9]) if values[9] else None
        for key, value in zip(("name", "roll", "department", "year", "contact"), values[1:6]):
            self.fields[key].delete(0, tk.END)
            self.fields[key].insert(0, value)
        self.bus.set(next((item for item in self.bus_values if item.startswith(f"{values[6]} |")), ""))
        self.route.set(next((item for item in self.route_values if item.endswith(f"| {values[7]}")), ""))
        self._load_stops()
        self.stop.set(next((item for item in self.stop_values if item.endswith(f"| {values[8]}")), ""))
        self._set_seat_value(values[9])

    def refresh(self):
        self.refresh_choices()
        rows = student_management.list_students(self.search.get())
        self.tree.delete(*self.tree.get_children())
        for row in rows:
            self.tree.insert("", tk.END, values=(
                row["id"], row["name"], row["roll_number"], row["department"], row["year"],
                row["contact_number"], row["bus_number"] or "", row["route_name"] or "",
                row["pickup_stop"] or "", row["seat_number"] or "",
            ))

    def import_csv(self):
        path = filedialog.askopenfilename(
            title="Import student CSV", filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        if not path:
            return
        try:
            imported = student_management.import_student_records(import_students(path))
            self.refresh()
            messagebox.showinfo("Import complete", f"Imported {imported} student record(s).")
        except Exception as error:
            show_error(error)
