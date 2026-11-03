import tkinter as tk
from tkinter import ttk
from typing import Callable

from CollegeBusManagement.gui.bus_window import BusWindow
from CollegeBusManagement.gui.fee_window import FeeWindow
from CollegeBusManagement.gui.reports_window import ReportsWindow
from CollegeBusManagement.gui.route_window import RouteWindow
from CollegeBusManagement.gui.seat_window import SeatWindow
from CollegeBusManagement.gui.student_window import StudentWindow


class Dashboard(ttk.Frame):
    MODULES = (
        ("Students", StudentWindow),
        ("Buses", BusWindow),
        ("Routes & Stops", RouteWindow),
        ("Seat Chart", SeatWindow),
        ("Fees", FeeWindow),
        ("Reports", ReportsWindow),
    )

    def __init__(self, parent, admin_username: str, on_logout: Callable[[], None]):
        super().__init__(parent)
        self.pack(fill=tk.BOTH, expand=True)
        self.on_logout = on_logout
        self.content = ttk.Frame(self, padding=12)

        header = ttk.Frame(self, padding=(12, 10))
        header.pack(side=tk.TOP, fill=tk.X)
        ttk.Label(
            header, text="College Bus Management System", font=("Segoe UI", 16, "bold")
        ).pack(side=tk.LEFT)
        ttk.Label(header, text=f"Admin: {admin_username}").pack(side=tk.RIGHT, padx=8)

        self.navigation = ttk.Frame(self, padding=(8, 4))
        self.navigation.pack(side=tk.TOP, fill=tk.X)
        for label, view_class in self.MODULES:
            ttk.Button(
                self.navigation,
                text=label,
                command=lambda cls=view_class: self.show_module(cls),
            ).pack(side=tk.LEFT, padx=3, pady=3)
        ttk.Button(self.navigation, text="Log out", command=self.on_logout).pack(
            side=tk.RIGHT, padx=3, pady=3
        )
        ttk.Separator(self, orient=tk.HORIZONTAL).pack(fill=tk.X)
        self.content.pack(fill=tk.BOTH, expand=True)
        ttk.Label(
            self.content,
            text="Choose a module above to manage transport records.",
            font=("Segoe UI", 12),
        ).pack(anchor=tk.W, pady=10)

    def show_module(self, view_class) -> None:
        for child in self.content.winfo_children():
            child.destroy()
        view_class(self.content).pack(fill=tk.BOTH, expand=True)
