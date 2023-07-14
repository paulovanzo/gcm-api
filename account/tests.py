from django.test import TestCase
from .models import Account

class AccountTestCase(TestCase):
    def test_create_account_normal(self):
        account = Account.create_account(number=1, account_type='normal')
        self.assertEqual(account.account_type, 'normal')
        self.assertEqual(account.balance, 0)
        self.assertEqual(account.points, 0)

    def test_create_account_bonus(self):
        account = Account.create_account(number=2, account_type='bonus')
        self.assertEqual(account.account_type, 'bonus')
        self.assertEqual(account.balance, 0)
        self.assertEqual(account.points, 10)

    def test_create_account_poupanca(self):
        account = Account.create_account(number=3, account_type='poupanca', initial_balance=100)
        self.assertEqual(account.account_type, 'poupanca')
        self.assertEqual(account.balance, 100)
        self.assertEqual(account.points, 0)

    def test_view_balance(self):
        account = Account.create_account(number=4, account_type='normal')
        balance = account.view_balance()
        self.assertEqual(balance, account.balance)

    def test_credit(self):
        account = Account.create_account(number=5, account_type='normal')
        account.credit(100)
        self.assertEqual(account.balance, 100)

    def test_credit_negative_value(self):
        account = Account.create_account(number=6, account_type='normal')
        with self.assertRaises(ValueError):
            account.credit(-100)

    def test_credit_bonus_account(self):
        account = Account.create_account(number=7, account_type='bonus')
        account.credit(100)
        self.assertEqual(account.balance, 100)
        self.assertEqual(account.points, 11)

    def test_debit(self):
        account = Account.create_account(number=8, account_type='poupanca', initial_balance=100)
        account.debit(50)
        self.assertEqual(account.balance, 50)

    def test_debit_negative_value(self):
        account = Account.create_account(number=9, account_type='normal', initial_balance=100)
        with self.assertRaises(ValueError):
            account.debit(-50)

    def test_debit_insufficient_balance(self):
        account = Account.create_account(number=10, account_type='poupanca', initial_balance=100)
        with self.assertRaises(ValueError):
            account.debit(150)

    def test_debit_poupanca_limit(self):
        account = Account.create_account(number=11, account_type='poupanca', initial_balance=100)
        account.debit(50)
        self.assertEqual(account.balance, 50)

        with self.assertRaises(ValueError):
            account.debit(51)

    def test_transfer(self):
        source_account = Account.create_account(number=12, account_type='poupanca', initial_balance=100)
        destination_account = Account.create_account(number=13, account_type='poupanca')
        source_account.transfer(destination_account, 50)

        self.assertEqual(source_account.balance, 50)
        self.assertEqual(destination_account.balance, 50)

    def test_transfer_negative_value(self):
        source_account = Account.create_account(number=14, account_type='normal', initial_balance=100)
        destination_account = Account.create_account(number=15, account_type='normal')
        with self.assertRaises(ValueError):
            source_account.transfer(destination_account, -50)

    def test_transfer_insufficient_balance(self):
        source_account = Account.create_account(number=16, account_type='normal', initial_balance=100)
        destination_account = Account.create_account(number=17, account_type='normal')
        with self.assertRaises(ValueError):
            source_account.transfer(destination_account, 150)

    def test_transfer_bonus_account(self):
        source_account = Account.create_account(number=18, account_type='poupanca', initial_balance=300)
        destination_account = Account.create_account(number=19, account_type='bonus')
        source_account.transfer(destination_account, 200)

        self.assertEqual(source_account.balance, 100)
        self.assertEqual(destination_account.balance, 200)
        self.assertEqual(destination_account.points, 11)

    def test_yield_interest_poupanca(self):
        account = Account.create_account(number=20, account_type='poupanca', initial_balance=100)
        account.yield_interest(2)
        self.assertEqual(account.balance, 102)

    def test_yield_interest_non_poupanca(self):
        account = Account.create_account(number=21, account_type='normal', initial_balance=100)
        with self.assertRaises(ValueError):
            account.yield_interest(2)