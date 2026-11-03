import hashlib
import hmac
import secrets

from CollegeBusManagement.database import DATABASE_PATH, connect, transaction
from CollegeBusManagement.utils.validation import require_text


HASH_ITERATIONS = 600_000
SALT_BYTES = 32
HASH_NAME = "sha256"
MIN_PASSWORD_LENGTH = 12
MAX_PASSWORD_LENGTH = 1024
MAX_USERNAME_LENGTH = 64


def _username(value: str) -> str:
    username = require_text(value, "Admin username")
    if len(username) > MAX_USERNAME_LENGTH:
        raise ValueError(f"Admin username cannot exceed {MAX_USERNAME_LENGTH} characters.")
    return username


def _password(value: str) -> str:
    if not value:
        raise ValueError("Password is required.")
    if len(value) < MIN_PASSWORD_LENGTH:
        raise ValueError(f"Password must contain at least {MIN_PASSWORD_LENGTH} characters.")
    if len(value) > MAX_PASSWORD_LENGTH:
        raise ValueError(f"Password cannot exceed {MAX_PASSWORD_LENGTH} characters.")
    return value


def admin_exists(database_path=DATABASE_PATH) -> bool:
    with connect(database_path) as connection:
        return connection.execute("SELECT 1 FROM admins LIMIT 1").fetchone() is not None


def create_admin(username: str, password: str, database_path=DATABASE_PATH) -> None:
    normalized_username = _username(username)
    valid_password = _password(password)
    salt = secrets.token_bytes(SALT_BYTES)
    password_hash = hashlib.pbkdf2_hmac(
        HASH_NAME, valid_password.encode("utf-8"), salt, HASH_ITERATIONS
    )
    with transaction(database_path) as connection:
        if connection.execute("SELECT 1 FROM admins LIMIT 1").fetchone():
            raise ValueError("An admin account already exists.")
        connection.execute(
            "INSERT INTO admins(username, password_salt, password_hash, hash_iterations) "
            "VALUES (?, ?, ?, ?)",
            (normalized_username, salt, password_hash, HASH_ITERATIONS),
        )


def authenticate_admin(username: str, password: str, database_path=DATABASE_PATH) -> bool:
    normalized_username = username.strip()
    if not normalized_username or not password or len(password) > MAX_PASSWORD_LENGTH:
        return False
    with connect(database_path) as connection:
        admin = connection.execute(
            "SELECT password_salt, password_hash, hash_iterations FROM admins "
            "WHERE username=? COLLATE NOCASE",
            (normalized_username,),
        ).fetchone()
    if admin is None:
        return False
    candidate = hashlib.pbkdf2_hmac(
        HASH_NAME,
        password.encode("utf-8"),
        admin["password_salt"],
        admin["hash_iterations"],
    )
    return hmac.compare_digest(candidate, admin["password_hash"])
