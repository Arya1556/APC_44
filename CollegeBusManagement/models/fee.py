from dataclasses import dataclass


@dataclass
class Fee:
    student_id: int
    total_fee: float
    amount_paid: float = 0.0
    payment_date: str | None = None

    @property
    def outstanding(self) -> float:
        return max(0.0, self.total_fee - self.amount_paid)

    @property
    def status(self) -> str:
        if self.amount_paid <= 0:
            return "Pending"
        if self.amount_paid < self.total_fee:
            return "Partially paid"
        return "Paid"
