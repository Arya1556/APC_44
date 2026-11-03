import tempfile
import unittest
from pathlib import Path

from CollegeBusManagement.database import connect, initialize_database
from CollegeBusManagement.modules.authentication import (
    admin_exists,
    authenticate_admin,
    create_admin,
)


class AuthenticationTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.database = Path(self.temporary.name) / "auth.db"
        initialize_database(self.database)

    def tearDown(self):
        self.temporary.cleanup()

    def test_create_admin_stores_only_salted_hash_and_authenticates(self):
        password = "Correct Horse Battery Staple 7"
        create_admin("transport-admin", password, self.database)
        self.assertTrue(admin_exists(self.database))
        self.assertTrue(authenticate_admin("TRANSPORT-ADMIN", password, self.database))
        self.assertFalse(authenticate_admin("transport-admin", "wrong password", self.database))
        with connect(self.database) as connection:
            admin = connection.execute(
                "SELECT password_salt, password_hash, hash_iterations FROM admins"
            ).fetchone()
        self.assertNotEqual(bytes(admin["password_hash"]), password.encode("utf-8"))
        self.assertEqual(len(admin["password_salt"]), 32)
        self.assertGreaterEqual(admin["hash_iterations"], 100_000)

    def test_password_minimum_and_single_admin_setup(self):
        with self.assertRaisesRegex(ValueError, "at least"):
            create_admin("admin", "short", self.database)
        create_admin("admin", "long-enough-demo-passphrase", self.database)
        with self.assertRaisesRegex(ValueError, "already exists"):
            create_admin("second", "another-long-demo-passphrase", self.database)


if __name__ == "__main__":
    unittest.main()
