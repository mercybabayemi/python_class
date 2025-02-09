import unittest

from account import Account


class AccountTest(unittest.TestCase):
    def setUp(self):
        self.account = Account("mercy", "Jane", "1234")

    def test_account_exists(self):
        self.assertEqual(self.account.get_account_number(), 0)
        self.assertEqual(self.account.get_first_name(), "mercy")
        self.assertEqual(self.account.get_last_name(), "Jane")

    def test_account_first_name_updates(self):
        self.account.update_first_name("mercy", "Mary")
        self.assertEqual(self.account.get_first_name(), "Mary")

    def test_account_deposits_successfully(self):
        self.account.deposit(5000)
        self.assertEqual(self.account.get_balance("1234"), 5000)

    def test_account_deposit_throws_exception(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-500)

    def test_account_withdraw_successfully(self):
        self.account.deposit(5000)
        self.account.withdraw(2000, "1234")
        self.assertEqual(self.account.get_balance("1234"), 3000)

    def test_account_withdraw_throws_exception_empty_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(5000, "1234")

    def test_account_withdraw_throws_exception_insufficient_balance(self):
        self.account.deposit(2000)
        with self.assertRaises(ValueError):
            self.account.withdraw(5000, "1234")

    def test_account_withdraw_throws_exception_incorrect_pin(self):
        self.account.deposit(5000)
        with self.assertRaises(ValueError):
            self.account.withdraw(5000, "1212")

    def test_account_withdraw_throws_exception_empty_pin(self):
        self.account.deposit(5000)
        with self.assertRaises(ValueError):
            self.account.withdraw(5000, "")

    def test_account_check_balance_returns_correct_value(self):
        self.account.deposit(5000)
        self.account.withdraw(2000, "1234")
        self.assertEqual(self.account.get_balance("1234"), 3000)

    def test_account_update_pin_successfully(self):
        self.account.update_pin("1234", "4321")
        self.account.deposit(500)
        self.account.withdraw(200, "4321")

    def test_account_update_pin_throws_exception_empty_old_pin(self):
        with self.assertRaises(ValueError):
            self.account.update_pin("", "4321")

    def test_account_update_pin_throws_exception_empty_new_pin(self):
        with self.assertRaises(ValueError):
            self.account.update_pin("1234", "")

    def test_account_get_account_number_returns_correct_value(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_account_number(), 0)
