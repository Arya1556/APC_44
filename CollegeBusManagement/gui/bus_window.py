import tkinter as tk
from tkinter import messagebox, ttk

from CollegeBusManagement.gui.bus_details_window import BusDetailsWindow
from CollegeBusManagement.gui.common import selected_id, show_error
from CollegeBusManagement.models.bus import Bus
from CollegeBusManagement.modules import bus_management, route_management


class BusWindow(ttk.Frame):
    COLUMNS = (
        "id", "number", "driver", "contact", "route",
        "capacity", "occupied", "vacant", "status",
    )
    HEADINGS = (
        "Bus ID", "Bus Number", "Driver Name", "Driver Contact", "Route Name",
        "Total Seats", "Occupied Seats", "Vacant Seats", "Bus Status",
    )

    def __init__(self, parent):
        super().__init__(parent, padding=8)
        self.bus_id = None
        form = ttk.LabelFrame(self, text="Bus details", padding=8)
        form.pack(fill=tk.X)
        self.entries = {}
        for index, (label, key) in enumerate((
            ("Bus number", "number"), ("Seating capacity", "capacity"),
            ("Driver name", "driver"), ("Driver contact", "contact"),
        )):
            ttk.Label(form, text=label).grid(row=0, column=index, sticky=tk.W)
            entry = ttk.Entry(form, width=20)
            entry.grid(row=1, column=index, padx=4)
            self.entries[key] = entry
        ttk.Label(form, text="Route").grid(row=0, column=4, sticky=tk.W)
        self.route = ttk.Combobox(form, width=24, state="readonly")
        self.route.grid(row=1, column=4, padx=4)

        actions = ttk.Frame(self)
        actions.pack(fill=tk.X, pady=5)
        for label, command in (("Add Bus", self.add), ("Edit Bus", self.update),
                               ("Delete Bus", self.delete), ("Clear", self.clear)):
            ttk.Button(actions, text=label, command=command).pack(side=tk.LEFT, padx=3)
        ttk.Label(actions, text="Search Bus").pack(side=tk.LEFT, padx=(18, 4))
        self.search = ttk.Entry(actions, width=28)
        self.search.pack(side=tk.LEFT)
        self.search.bind("<Return>", lambda _event: self.refresh())
        ttk.Button(actions, text="Refresh", command=self.refresh).pack(side=tk.LEFT, padx=4)
        ttk.Button(actions, text="Show All", command=self.show_all).pack(side=tk.LEFT, padx=4)
        ttk.Button(actions, text="View Details", command=self.view_details).pack(side=tk.LEFT, padx=4)

        table_frame = ttk.Frame(self)
        table_frame.pack(fill=tk.BOTH, expand=True, padx=8, pady=6)
        self.tree = ttk.Treeview(
            table_frame, columns=self.COLUMNS, show="headings", height=12
        )
        vertical_scrollbar = ttk.Scrollbar(
            table_frame, orient=tk.VERTICAL, command=self.tree.yview
        )
        horizontal_scrollbar = ttk.Scrollbar(
            table_frame, orient=tk.HORIZONTAL, command=self.tree.xview
        )
        self.tree.configure(
            yscrollcommand=vertical_scrollbar.set,
            xscrollcommand=horizontal_scrollbar.set,
        )
        self.tree.bind("<<TreeviewSelect>>", self._select)
        self.tree.bind("<Double-1>", lambda _event: self.view_details())
        for column, heading in zip(self.COLUMNS, self.HEADINGS):
            self.tree.heading(column, text=heading)
            self.tree.column(column, width=145, minwidth=100, anchor=tk.W)
        self.tree.grid(row=0, column=0, sticky="nsew")
        vertical_scrollbar.grid(row=0, column=1, sticky="ns")
        horizontal_scrollbar.grid(row=1, column=0, sticky="ew")
        table_frame.rowconfigure(0, weight=1)
        table_frame.columnconfigure(0, weight=1)
        self.refresh()

    def refresh(self):
        self.routes = route_management.list_routes()
        self.route_values = [f"{row['id']} | {row['route_name']}" for row in self.routes]
        self.route["values"] = self.route_values
        self.tree.delete(*self.tree.get_children())
        for row in bus_management.list_buses(search=self.search.get()):
            self.tree.insert("", tk.END, values=(
                row["id"], row["bus_number"], row["driver_name"], row["driver_contact"],
                row["route_name"] or "", row["seating_capacity"], row["occupied_seats"],
                row["available_seats"], row["bus_status"],
            ))

    def show_all(self):
        self.search.delete(0, tk.END)
        self.refresh()

    def _bus(self):
        try:
            route_id = int(self.route.get().split(" | ", 1)[0])
        except (ValueError, IndexError):
            route_id = None
        return Bus(
            self.entries["number"].get(), self.entries["capacity"].get(),
            self.entries["driver"].get(), self.entries["contact"].get(), route_id,
        )

    def add(self):
        try:
            bus_management.add_bus(self._bus())
            self.clear()
            self.refresh()
        except Exception as error:
            show_error(error)

    def update(self):
        if self.bus_id is None:
            messagebox.showinfo("Select a bus", "Select a bus record first.")
            return
        try:
            bus_management.update_bus(self.bus_id, self._bus())
            self.refresh()
        except Exception as error:
            show_error(error)

    def delete(self):
        bus_id = selected_id(self.tree)
        if bus_id is None:
            messagebox.showinfo("Select a bus", "Select a bus record first.")
            return
        if not messagebox.askyesno(
            "Confirm bus deletion",
            "Delete this bus? Any students assigned to it will remain in the system "
            "but their bus and seat allocations will be released.",
        ):
            return
        try:
            bus_management.delete_bus(bus_id)
            self.clear()
            self.refresh()
        except Exception as error:
            show_error(error)

    def view_details(self):
        bus_id = selected_id(self.tree)
        if bus_id is None:
            messagebox.showinfo("Select a bus", "Select a bus to view its details.")
            return
        try:
            BusDetailsWindow(self.winfo_toplevel(), bus_id)
        except Exception as error:
            show_error(error)

    def _select(self, _event):
        selection = self.tree.selection()
        if not selection:
            return
        values = self.tree.item(selection[0], "values")
        self.bus_id = int(values[0])
        for key, value in zip(("number", "driver", "contact"), values[1:4]):
            self.entries[key].delete(0, tk.END)
            self.entries[key].insert(0, value)
        self.entries["capacity"].delete(0, tk.END)
        self.entries["capacity"].insert(0, values[5])
        self.route.set(next(
            (value for value in self.route_values if value.endswith(f"| {values[4]}")), ""
        ))

    def clear(self):
        self.bus_id = None
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.route.set("")
