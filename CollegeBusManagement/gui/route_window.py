import tkinter as tk
from tkinter import messagebox, ttk

from CollegeBusManagement.gui.common import make_tree, selected_id, show_error
from CollegeBusManagement.models.route import Route
from CollegeBusManagement.modules import route_management


class RouteWindow(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=8)
        form = ttk.LabelFrame(self, text="Route", padding=8)
        form.pack(fill=tk.X)
        self.route_entries = []
        for index, label in enumerate(("Route name", "Starting point", "Destination")):
            ttk.Label(form, text=label).grid(row=0, column=index, sticky=tk.W)
            entry = ttk.Entry(form, width=25)
            entry.grid(row=1, column=index, padx=4)
            self.route_entries.append(entry)
        ttk.Button(form, text="Add route", command=self.add_route).grid(row=1, column=3, padx=4)
        ttk.Button(form, text="Update selected", command=self.update_route).grid(row=1, column=4, padx=4)
        ttk.Button(form, text="Delete selected", command=self.delete_route).grid(row=1, column=5, padx=4)
        self.routes_tree = make_tree(
            self, ("id", "name", "start", "destination", "buses", "stop_count"),
            ("Route ID", "Route Name", "Starting Point", "Destination", "Assigned Bus", "Stops"),
        )
        self.routes_tree.bind("<<TreeviewSelect>>", self._select_route)
        stop_form = ttk.LabelFrame(self, text="Add stop to selected route", padding=8)
        stop_form.pack(fill=tk.X, pady=6)
        self.stop_name = ttk.Entry(stop_form, width=24)
        self.stop_order = ttk.Entry(stop_form, width=10)
        ttk.Label(stop_form, text="Stop name").pack(side=tk.LEFT)
        self.stop_name.pack(side=tk.LEFT, padx=4)
        ttk.Label(stop_form, text="Order").pack(side=tk.LEFT)
        self.stop_order.pack(side=tk.LEFT, padx=4)
        ttk.Button(stop_form, text="Add stop", command=self.add_stop).pack(side=tk.LEFT, padx=4)
        ttk.Button(stop_form, text="Delete selected stop", command=self.delete_stop).pack(side=tk.LEFT, padx=4)
        self.stops_tree = make_tree(
            self, ("id", "name", "order"), ("Stop ID", "Stop Name", "Stop Order")
        )
        self.refresh()

    def refresh(self):
        self.routes_tree.delete(*self.routes_tree.get_children())
        for row in route_management.list_routes():
            self.routes_tree.insert("", tk.END, values=(
                row["id"], row["route_name"], row["starting_point"], row["destination"],
                row["assigned_buses"] or "Not assigned", row["stop_count"],
            ))
        self._refresh_stops(selected_id(self.routes_tree))

    def add_route(self):
        try:
            route_management.add_route(Route(*(entry.get() for entry in self.route_entries)))
            self.refresh()
        except Exception as error:
            show_error(error)

    def update_route(self):
        route_id = selected_id(self.routes_tree)
        if route_id is None:
            messagebox.showinfo("Select a route", "Select a route record first.")
            return
        try:
            route_management.update_route(
                route_id, Route(*(entry.get() for entry in self.route_entries))
            )
            self.refresh()
        except Exception as error:
            show_error(error)

    def delete_route(self):
        route_id = selected_id(self.routes_tree)
        if route_id is None:
            messagebox.showinfo("Select a route", "Select a route record first.")
            return
        if messagebox.askyesno("Confirm deletion", "Delete route and its stops?"):
            try:
                route_management.delete_route(route_id)
                self.refresh()
            except Exception as error:
                show_error(error)

    def _select_route(self, _event):
        selection = self.routes_tree.selection()
        if not selection:
            return
        values = self.routes_tree.item(selection[0], "values")
        for entry, value in zip(self.route_entries, values[1:]):
            entry.delete(0, tk.END)
            entry.insert(0, value)
        self._refresh_stops(int(values[0]))

    def _refresh_stops(self, route_id):
        self.stops_tree.delete(*self.stops_tree.get_children())
        if route_id is None:
            return
        for row in route_management.list_stops(route_id):
            self.stops_tree.insert(
                "", tk.END, values=(row["id"], row["stop_name"], row["stop_order"])
            )

    def add_stop(self):
        route_id = selected_id(self.routes_tree)
        if route_id is None:
            messagebox.showinfo("Select a route", "Select a route before adding a stop.")
            return
        try:
            route_management.add_stop(
                route_id, self.stop_name.get(), self.stop_order.get()
            )
            self.refresh()
        except Exception as error:
            show_error(error)

    def delete_stop(self):
        stop_id = selected_id(self.stops_tree)
        if stop_id is None:
            messagebox.showinfo("Select a stop", "Select a stop record first.")
            return
        try:
            route_management.delete_stop(stop_id)
            self.refresh()
        except Exception as error:
            show_error(error)
