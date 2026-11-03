import tkinter as tk
from pathlib import Path
from tkinter import messagebox, ttk

from CollegeBusManagement.gui.common import make_tree
from CollegeBusManagement.modules.reports import (
    dashboard_summary,
    export_chart,
    export_fee_chart,
)
from CollegeBusManagement.modules.student_management import list_students
from CollegeBusManagement.utils.file_handler import export_students


class ReportsWindow(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, padding=10)
        self.summary = ttk.Label(self, text="", justify=tk.LEFT, font=("Segoe UI", 11))
        self.summary.pack(anchor=tk.W, pady=(0, 8))
        actions = ttk.Frame(self)
        actions.pack(fill=tk.X, pady=4)
        ttk.Button(actions, text="Refresh reports", command=self.refresh).pack(side=tk.LEFT, padx=3)
        ttk.Button(actions, text="Export students CSV", command=self.export_csv).pack(side=tk.LEFT, padx=3)
        ttk.Button(actions, text="Save occupancy chart", command=self.export_occupancy).pack(side=tk.LEFT, padx=3)
        ttk.Button(actions, text="Save fee chart", command=self.export_fees).pack(side=tk.LEFT, padx=3)
        ttk.Label(self, text="Students by route").pack(anchor=tk.W, pady=(10, 0))
        self.routes = make_tree(
            self, ("route", "students"), ("Route", "Student Count")
        )
        self.refresh()

    def refresh(self):
        data = dashboard_summary()
        self.summary.configure(text=(
            f"Total students: {data['students']}    Total buses: {data['buses']}    "
            f"Total routes: {data['routes']}\n"
            f"Occupied seats: {data['occupied_seats']}    Vacant seats: {data['vacant_seats']}\n"
            f"Fees collected: {data['fees_collected']:.2f}    "
            f"Fees outstanding: {data['fees_outstanding']:.2f}"
        ))
        self.routes.delete(*self.routes.get_children())
        for row in data["route_students"].itertuples(index=False):
            self.routes.insert("", tk.END, values=(row.route_name, row.students))

    def export_csv(self):
        try:
            rows = [dict(row) for row in list_students()]
            destination = Path(__file__).resolve().parents[1] / "exports" / "students.csv"
            export_students(rows, destination)
            messagebox.showinfo("Export complete", f"Student records exported to:\n{destination}")
        except Exception as error:
            messagebox.showerror("Export failed", str(error), parent=self)

    def export_occupancy(self):
        try:
            path = export_chart(Path(__file__).resolve().parents[1] / "charts" / "bus_occupancy.png")
            messagebox.showinfo("Chart saved", f"Occupancy chart saved to:\n{path}", parent=self)
        except Exception as error:
            messagebox.showerror("Chart failed", str(error), parent=self)

    def export_fees(self):
        try:
            path = export_fee_chart(Path(__file__).resolve().parents[1] / "charts" / "fee_summary.png")
            messagebox.showinfo("Chart saved", f"Fee summary chart saved to:\n{path}", parent=self)
        except Exception as error:
            messagebox.showerror("Chart failed", str(error), parent=self)
