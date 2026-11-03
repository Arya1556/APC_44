import tkinter as tk
from tkinter import ttk

from CollegeBusManagement.modules.bus_management import list_buses
from CollegeBusManagement.modules.seat_allocation import seating_chart


class SeatWindow(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=12)
        ttk.Label(self, text="Bus").pack(side=tk.LEFT)
        self.bus = ttk.Combobox(self, width=30, state="readonly")
        self.bus.pack(side=tk.LEFT, padx=6)
        self.bus.bind("<<ComboboxSelected>>", lambda _event: self.refresh())
        self.canvas = ttk.Frame(self)
        self.canvas.pack(fill=tk.BOTH, expand=True, pady=10)
        self.refresh_buses()

    def refresh_buses(self):
        self.buses = list_buses()
        self.values = [f"{row['id']} | {row['bus_number']}" for row in self.buses]
        self.bus["values"] = self.values
        if self.values and self.bus.get() not in self.values:
            self.bus.set(self.values[0])
        self.refresh()

    def refresh(self):
        for child in self.canvas.winfo_children():
            child.destroy()
        try:
            bus_id = int(self.bus.get().split(" | ", 1)[0])
        except (ValueError, IndexError):
            return
        for seat in seating_chart(bus_id):
            label = f"Seat {seat['seat_number']}\n{seat['student'] or 'Vacant'}"
            color = "#f4a6a6" if seat["occupied"] else "#a8dfad"
            tk.Button(
                self.canvas, text=label, bg=color, width=14, height=3,
                relief=tk.RIDGE, state=tk.DISABLED,
            ).grid(row=(seat["seat_number"] - 1) // 5, column=(seat["seat_number"] - 1) % 5,
                   padx=5, pady=5)
