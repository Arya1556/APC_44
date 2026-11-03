import tkinter as tk
from tkinter import messagebox, ttk

from CollegeBusManagement.modules.bus_management import get_bus_details, get_bus_seating


class BusDetailsWindow(tk.Toplevel):
    def __init__(self, parent, bus_id: int):
        super().__init__(parent)
        self.bus_id = bus_id
        self.title("Bus Details and Seating")
        self.geometry("760x700")
        self.minsize(560, 460)
        self.transient(parent)
        self._build()
        self.refresh()

    def _build(self):
        self.details = ttk.LabelFrame(self, text="Bus information", padding=10)
        self.details.pack(fill=tk.X, padx=10, pady=10)
        self.summary = ttk.Label(self.details, text="", justify=tk.LEFT)
        self.summary.pack(anchor=tk.W)

        toolbar = ttk.Frame(self)
        toolbar.pack(fill=tk.X, padx=10)
        ttk.Label(toolbar, text="Seating layout (green = vacant, red = occupied)").pack(side=tk.LEFT)
        ttk.Button(toolbar, text="Refresh", command=self.refresh).pack(side=tk.RIGHT)

        container = ttk.Frame(self)
        container.pack(fill=tk.BOTH, expand=True, padx=10, pady=8)
        self.canvas = tk.Canvas(container, highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient=tk.VERTICAL, command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.seats_frame = ttk.Frame(self.canvas)
        self.canvas_window = self.canvas.create_window(
            (0, 0), window=self.seats_frame, anchor=tk.NW
        )
        self.seats_frame.bind(
            "<Configure>",
            lambda _event: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )
        self.canvas.bind(
            "<Configure>",
            lambda event: self.canvas.itemconfigure(self.canvas_window, width=event.width),
        )

    def refresh(self):
        details = get_bus_details(self.bus_id)
        self.summary.configure(text=(
            f"Bus number: {details['bus_number']}    "
            f"Driver: {details['driver_name']} ({details['driver_contact']})\n"
            f"Assigned route: {details['route_name'] or 'Not assigned'}    "
            f"Total seats: {details['seating_capacity']}    "
            f"Occupied: {details['occupied_seats']}    "
            f"Vacant: {details['available_seats']}"
        ))
        for child in self.seats_frame.winfo_children():
            child.destroy()
        for seat in get_bus_seating(self.bus_id):
            if seat["occupied"]:
                student = seat["student"]
                label = f"Seat {seat['seat_number']}\nOccupied"
                color = "#f4a6a6"
                details_text = (
                    f"Student: {student['name']}\n"
                    f"Roll number: {student['roll_number']}\n"
                    f"Seat number: {seat['seat_number']}"
                )
            else:
                label = f"Seat {seat['seat_number']}\nVacant"
                color = "#a8dfad"
                details_text = f"Seat {seat['seat_number']} is available."
            tk.Button(
                self.seats_frame,
                text=label,
                bg=color,
                activebackground=color,
                width=14,
                height=3,
                command=lambda text=details_text: messagebox.showinfo(
                    "Seat information", text, parent=self
                ),
            ).grid(
                row=(seat["seat_number"] - 1) // 5,
                column=(seat["seat_number"] - 1) % 5,
                padx=6,
                pady=6,
                sticky="nsew",
            )
        for column in range(5):
            self.seats_frame.columnconfigure(column, weight=1)
