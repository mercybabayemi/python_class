import unittest

from account import Account
from bank import Bank


class TestBank(unittest.TestCase):
    def setUp(self):
        self.bank = Bank(Account("Mercy", "Janet", "1234"))

    def test_bank_accounts_empty(self):
        self.assertTrue(self.bank.is_accounts_empty())

    def test_bank_account_creation_and_size(self):
        account1 = self.bank.create_account("Mercy", "Janet", "1234")
        account2 = self.bank.create_account("Yomi", "Olaide", "3245")
        self.assertEqual(self.bank.get_size(), 2)

    def test_bank_account_removal(self):
        account_number_1 = self.bank.create_account( "Mercy", "Janet", "1234")
        account_number_2 = self.bank.create_account("Yomi", "Olaide", "3245")
        self.assertEqual(self.bank.get_size(), 2)
        self.bank.remove(account_number_2)
        self.assertEqual(self.bank.get_size(), 1)

    def test_bank_account_removal_throws_exception(self):
        with self.assertRaises(ValueError):
            self.bank.remove("")

    def test_bank_find_account_by_account_number(self):
        account1 = self.bank.create_account("Mercy", "Janet", "1234")
        found_account = self.bank.find_account_by_account_number(account1)
        self.assertEqual(found_account.get_account_number(), 1)

    def test_bank_deposit(self):
        account_1 = self.bank.create_account("Mercy", "Janet", "1234")
        self.bank.deposit(account_1, 5000)
        self.assertEqual(self.bank.check_balance(account_1, "1234"), 5000)

    def test_bank_deposit_throws_exception_when_wrong_pin(self):
        account_1 = self.bank.create_account("Mercy", "Janet", "1234")
        with self.assertRaises(ValueError):
            self.bank.deposit(account_1, -1)

    def test_bank_withdraw(self):
        account1 = self.bank.create_account("Mercy", "Janet", "1234")
        self.bank.deposit(account1, 5000)
        self.bank.withdraw(account1, 2000, "1234")
        self.assertEqual(self.bank.check_balance(account1, "1234"), 3000)

    def test_bank_transfer(self):
        account1 = self.bank.create_account("Mercy", "Janet", "1234")
        account2 = self.bank.create_account("Yomi", "Olaide", "3245")
        self.bank.deposit(account1, 5000)
        self.bank.deposit(account2, 2000)
        self.bank.transfer(account1, account2, 1000, "1234")
        self.assertEqual(self.bank.check_balance(account1, "1234"), 4000)
        self.assertEqual(self.bank.check_balance(account2, "3245"), 3000)

    def test_bank_transfer_throws_exception_when_same_account(self):
        account1 = self.bank.create_account("Mercy", "Janet", "1234")
        with self.assertRaises(ValueError):
            self.bank.transfer(account1, account1, 2000, "1234")