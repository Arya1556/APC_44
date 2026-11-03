import tkinter as tk
from tkinter import messagebox

from CollegeBusManagement.database import initialize_database
from CollegeBusManagement.gui.dashboard import Dashboard
from CollegeBusManagement.gui.login_window import LoginWindow


def main():
    try:
        initialize_database()
    except Exception as error:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Database error", str(error))
        root.destroy()
        raise
    root = tk.Tk()
    root.withdraw()

    def close_application():
        root.destroy()

    def open_application(username: str):
        root.withdraw()
        window = tk.Toplevel(root)
        window.title("College Bus Management System")
        window.geometry("1200x800")
        window.minsize(900, 600)

        def logout():
            window.destroy()
            root.deiconify()

        window.protocol("WM_DELETE_WINDOW", close_application)
        Dashboard(window, username, logout)

    LoginWindow(root, open_application)
    root.deiconify()
    root.mainloop()


if __name__ == "__main__":
    main()


"""powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r .\CollegeBusManagement\requirements.txt
py -m CollegeBusManagement.main
"""