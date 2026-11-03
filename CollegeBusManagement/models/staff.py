class TransportStaff:
    def __init__(self, name: str, contact_number: str):
        self.name = name
        self.contact_number = contact_number

    def role_summary(self) -> str:
        return f"Transport staff: {self.name}"


class Admin(TransportStaff):
    def role_summary(self) -> str:
        return f"Administrator: {self.name} (can manage transport records)"
