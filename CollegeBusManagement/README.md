# College Bus Management System

A beginner-friendly Tkinter desktop application with SQLite persistence. The main app uses Python's built-in `tkinter`, `sqlite3`, `csv`, and `re` modules plus NumPy, Pandas, and Matplotlib. A separate Django case study demonstrates the ORM/SQLite workflow. Optional self-study examples are kept out of the core app.

## Architecture

```text
Tkinter screens (gui/)
        |
Operations and validation (modules/, utils/)
        |
SQLite database (database.py -> college_bus.db)

Separate demonstrations:
django_case_study/     Django ORM with its own SQLite database
self_study/            NLTK, scikit-learn, Pygame, Python syllabus examples
```

The GUI calls small operation modules; the modules own validation and database work. `database.py` creates the schema and uses foreign keys and transactions. The Django case study has a separate database and does not power the Tkinter application.

## Folder and file guide

| Path | Purpose |
|---|---|
| `main.py` | Applies the additive database schema initialization and launches the admin login. |
| `database.py` | SQLite connection, schema creation, transactions, and example records. |
| `models/` | `Student`, `Bus`, `Route`, `Stop`, `Fee`, and staff classes. |
| `modules/authentication.py` | Admin account setup and PBKDF2-HMAC password verification. |
| `modules/` | Student, bus, route/stop, seat, fee, and report operations. |
| `gui/` | Admin login, module navigation, bus seating details, and feature views. |
| `utils/validation.py` | Required-field, number, contact, roll, and bus-number validation. |
| `utils/file_handler.py` | UTF-8 CSV import/export helpers. |
| `tests/` | Core database/seat workflow tests. |
| `exports/` | Student CSV exports. |
| `charts/` | Generated bus-occupancy and fee-summary charts. |
| `django_case_study/` | Independent Django project and `transport` app. |
| `self_study/` | Optional NLTK, demand-prediction, Pygame, and Python concept samples. |

## Database schema and relationships

- `routes` has many `stops`, `buses`, and `students`.
- Each `stop` belongs to one route; `(route_id, stop_order)` and `(route_id, stop_name)` are unique.
- Each `bus` can be assigned to one route; bus numbers are unique and capacity must be positive.
- Each `student` has a unique roll number and may be assigned a bus, route, pickup stop, and seat.
- `UNIQUE(bus_id, seat_number)` prevents duplicate occupied seats on one bus while allowing seat numbers to repeat on different buses. A database check requires both bus and seat to be set or both to be empty.
- Each `fee` record belongs to one student. Paid amounts are constrained between zero and the total.

Deleting a bus releases its students' seats. Changing a bus route with assigned students is refused until those students are reassigned or removed. Student creation and assignment are transactional; automatic assignment chooses the lowest free seat within capacity.

## Install and run on Windows

Use Python 3.10 or later. Open PowerShell in the directory containing this `CollegeBusManagement` folder:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install -r .\CollegeBusManagement\requirements.txt
py -m CollegeBusManagement.main
```

If PowerShell blocks activation, run `py .\CollegeBusManagement\main.py` from the parent folder after installing dependencies. The app creates `CollegeBusManagement\college_bus.db` on first launch. On an existing installation, initialization adds an `admins` table using `CREATE TABLE IF NOT EXISTS`; it does not drop, reset, or rewrite student, bus, route, stop, or fee records.

If there is no admin account yet, the first screen asks you to create one. Choose your own username and password (at least 12 characters) and confirm the password. The app stores a unique random salt and a PBKDF2-HMAC-SHA256 hash in SQLite, not the original password. After setup, log in using those credentials. The main application opens only after successful authentication; use **Log out** to return to login.

On a fresh install, there are no transport records. If you want sample route, stops, and bus records for a fresh database, from the parent folder run:

```powershell
py -c "from CollegeBusManagement.database import initialize_database, seed_sample_data; initialize_database(); seed_sample_data()"
```

Do not run the sample-data command if you do not want demonstration records. It only inserts samples when the route table is empty and never resets an existing database. Use the navigation buttons to open one module at a time. **Buses** lists all registered buses, calculates occupied seats from actual student seat allocations, supports searching, and opens an individual seating view when a row is double-clicked or **View Details** is used. Seat allocation is automatic by default. An authenticated admin can use **Authorize manual seats** in Students to enable manual seat selection for that session. Student CSV import expects the columns exported by this application.

## Features and expected behavior

- Add, update, search, and delete student and bus records; route/stop and fee records have add/update/delete controls where appropriate.
- Stops are ordered within their route. A student's pickup stop must belong to the selected route, and an assigned bus must also use that route.
- Seat chart distinguishes occupied and vacant seats; a full bus rejects another student.
- Fee records show paid, partially paid, and pending status and outstanding balance.
- The main window shows clean module navigation without record, occupancy, route, or fee statistics. Those report summaries and charts are inside **Reports**.
- Student CSV import/export uses `exports/students.csv` for export. Reports can save occupancy and fee charts under `charts/`.
- Input and database errors are shown in the UI rather than silently ignored.

## Run tests

From the parent directory:

```powershell
py -m unittest discover -s .\CollegeBusManagement\tests -v
```

Tests use temporary databases and verify automatic lowest-seat allocation, capacity enforcement, re-use of seat numbers across different buses, and seat release on assignment removal.
They also check hashed admin login and incorrect-password rejection, actual bus occupancy/search, and that database initialization adds the admin table without removing existing student data.

## Django and SQLite case study (separate)

Install its extra dependency from the parent folder:

```powershell
py -m pip install -r .\CollegeBusManagement\requirements-django.txt
Set-Location .\CollegeBusManagement\django_case_study
py .\manage.py migrate
py .\manage.py runserver
```

The case study defines an ORM model and JSON views for create, read, update, and delete at `/api/students/` and `/api/students/<id>/`. It intentionally does not provide browser templates. A production web interface would normally use Django templates, which are outside the main Tkinter application's scope. Django creates its own `django_case_study\db.sqlite3`.

## Optional syllabus demonstrations

Install only when using the optional examples:

```powershell
py -m pip install -r .\CollegeBusManagement\requirements-self-study.txt
py -m CollegeBusManagement.self_study.syllabus_basics
py -m CollegeBusManagement.self_study.nltk_demo
py -m CollegeBusManagement.self_study.demand_prediction
py -m CollegeBusManagement.self_study.pygame_simulation
```

The demand model uses tiny illustrative sample data and is not an operational forecast.

## Syllabus-to-code mapping

| Syllabus topic | Example location |
|---|---|
| Variables, data types, strings, lists, tuples, sets, dictionaries, functions, lambda, control flow | `self_study/syllabus_basics.py`, `models/`, `modules/` |
| Arrays and numerical calculations | `modules/reports.py` (NumPy) |
| Classes and objects | `models/student.py`, `models/bus.py`, `models/route.py`, `models/fee.py` |
| Default arguments / Python method dispatch | `models/bus.py` (`available_seats(occupied=0)`); Python does not dispatch overloaded methods by signature |
| Inheritance and polymorphism | `models/staff.py` (`Admin.role_summary` overrides the base implementation) |
| Files and CSV | `utils/file_handler.py`, `gui/student_window.py`, `gui/dashboard.py` |
| Exceptions and validation with `re` | `utils/validation.py`, `modules/`, and the GUI error dialogs |
| Tkinter desktop GUI | `gui/` |
| SQLite connectivity and SQL CRUD | `database.py`, `modules/` |
| Django ORM and SQLite | `django_case_study/` |
| Pandas tables and summaries | `modules/reports.py` |
| Matplotlib charts | `modules/reports.py` |
| NLTK, Scikit-learn, Pygame | `self_study/nltk_demo.py`, `self_study/demand_prediction.py`, `self_study/pygame_simulation.py` |

## Short project report

**Problem:** College transport records and seat assignments need a consistent way to track students, vehicles, stops, and payments.

**Solution:** A modular Tkinter application stores records in SQLite, checks relationships and seat capacity, and uses Pandas/NumPy/Matplotlib for summaries. A separate Django case study demonstrates the web framework and ORM.

**Limitations:** The local admin login protects access through this application but does not encrypt the SQLite file itself; users with direct file access can inspect or alter its records. The optional demand-prediction sample is educational and not suitable for real planning. The Django endpoints are a learning example, not a production-ready service.

## Viva questions

1. **Why use SQLite?** It is a file-based relational database available through Python's standard library.
2. **How is seat duplication prevented?** A unique constraint on `(bus_id, seat_number)` plus transaction-based allocation.
3. **Why use a foreign key for a pickup stop?** It prevents references to stops that do not exist; application validation also checks that the stop belongs to the selected route.
4. **What does Pandas provide?** DataFrame-based tables and summaries for records.
5. **Why is the Django database separate?** The Django ORM demonstration is independent of the Tkinter app's `sqlite3` layer.
6. **Does Python support traditional method overloading by signature?** No; default arguments or `*args` can express flexible calls, while Python uses the latest method definition for a given name.
