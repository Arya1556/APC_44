import re


ROLL_PATTERN = re.compile(r"^[A-Za-z0-9/-]{2,20}$")
CONTACT_PATTERN = re.compile(r"^\+?[0-9][0-9\s-]{7,14}$")
BUS_PATTERN = re.compile(r"^[A-Za-z0-9-]{2,15}$")


def require_text(value: str, label: str) -> str:
    cleaned = value.strip()
    if not cleaned:
        raise ValueError(f"{label} is required.")
    return cleaned


def validate_roll_number(value: str) -> str:
    cleaned = require_text(value, "Roll number")
    if not ROLL_PATTERN.fullmatch(cleaned):
        raise ValueError("Roll number must be 2-20 letters, digits, / or -.")
    return cleaned


def validate_contact(value: str) -> str:
    cleaned = require_text(value, "Contact number")
    if not CONTACT_PATTERN.fullmatch(cleaned):
        raise ValueError("Enter a valid contact number (8-15 digits, spaces or hyphens allowed).")
    return cleaned


def validate_bus_number(value: str) -> str:
    cleaned = require_text(value, "Bus number")
    if not BUS_PATTERN.fullmatch(cleaned):
        raise ValueError("Bus number must be 2-15 letters, digits or hyphens.")
    return cleaned


def positive_integer(value: str, label: str) -> int:
    try:
        number = int(value)
    except ValueError as exc:
        raise ValueError(f"{label} must be a whole number.") from exc
    if number <= 0:
        raise ValueError(f"{label} must be greater than zero.")
    return number


def non_negative_amount(value: str, label: str) -> float:
    try:
        amount = float(value)
    except ValueError as exc:
        raise ValueError(f"{label} must be a number.") from exc
    if amount < 0:
        raise ValueError(f"{label} cannot be negative.")
    return amount
