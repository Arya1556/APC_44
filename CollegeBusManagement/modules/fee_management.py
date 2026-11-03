from CollegeBusManagement.database import DATABASE_PATH, connect, transaction
from CollegeBusManagement.models.fee import Fee
from CollegeBusManagement.utils.validation import non_negative_amount


def add_fee(fee: Fee, database_path=DATABASE_PATH) -> int:
    total = non_negative_amount(str(fee.total_fee), "Total fee")
    paid = non_negative_amount(str(fee.amount_paid), "Amount paid")
    if paid > total:
        raise ValueError("Amount paid cannot exceed total fee.")
    with transaction(database_path) as connection:
        if not connection.execute("SELECT 1 FROM students WHERE id=?", (fee.student_id,)).fetchone():
            raise LookupError("Student was not found.")
        cursor = connection.execute(
            "INSERT INTO fees(student_id, total_fee, amount_paid, payment_date) "
            "VALUES (?, ?, ?, COALESCE(?, CURRENT_DATE))",
            (fee.student_id, total, paid, fee.payment_date),
        )
        return int(cursor.lastrowid)


def update_fee(fee_id: int, fee: Fee, database_path=DATABASE_PATH) -> None:
    total = non_negative_amount(str(fee.total_fee), "Total fee")
    paid = non_negative_amount(str(fee.amount_paid), "Amount paid")
    if paid > total:
        raise ValueError("Amount paid cannot exceed total fee.")
    with transaction(database_path) as connection:
        cursor = connection.execute(
            "UPDATE fees SET student_id=?, total_fee=?, amount_paid=?, "
            "payment_date=COALESCE(?, payment_date) WHERE id=?",
            (fee.student_id, total, paid, fee.payment_date, fee_id),
        )
        if not cursor.rowcount:
            raise LookupError("Fee record was not found.")


def delete_fee(fee_id: int, database_path=DATABASE_PATH) -> None:
    with transaction(database_path) as connection:
        cursor = connection.execute("DELETE FROM fees WHERE id=?", (fee_id,))
        if not cursor.rowcount:
            raise LookupError("Fee record was not found.")


def list_fees(database_path=DATABASE_PATH) -> list:
    with connect(database_path) as connection:
        return connection.execute(
            "SELECT f.*, s.name, s.roll_number, "
            "f.total_fee-f.amount_paid AS outstanding, "
            "CASE WHEN f.amount_paid=0 THEN 'Pending' "
            "WHEN f.amount_paid<f.total_fee THEN 'Partially paid' ELSE 'Paid' END AS status "
            "FROM fees f JOIN students s ON s.id=f.student_id ORDER BY s.name, f.payment_date"
        ).fetchall()


def fee_totals(database_path=DATABASE_PATH) -> dict[str, float]:
    with connect(database_path) as connection:
        row = connection.execute(
            "SELECT COALESCE(SUM(amount_paid), 0) AS collected, "
            "COALESCE(SUM(total_fee-amount_paid), 0) AS outstanding FROM fees"
        ).fetchone()
        return {"collected": float(row["collected"]), "outstanding": float(row["outstanding"])}
