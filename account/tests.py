from django.test import TestCase
from decimal import Decimal
from .models import Account

class BankOperationsTestCase(TestCase):
    def setUp(self):
        self.normal_account = Account.objects.create(number=42345, balance=100.00, account_type='normal', points=0)
        self.bonus_account = Account.objects.create(number=57890, balance=200.00, account_type='bonus', points=0)
        self.poupanca_account = Account.objects.create(number=64680, balance=500.00, account_type='poupanca', points=0)

    def test_cadastrar_conta_normal(self):
        account = Account.objects.create(number=13579, account_type='normal')
        self.assertEqual(account.account_type, 'normal')
        self.assertEqual(account.balance, Decimal('0.00'))

    def test_cadastrar_conta_bonus(self):
        account = Account.objects.create(number=24680, account_type='bonus')
        self.assertEqual(account.account_type, 'bonus')
        self.assertEqual(account.balance, Decimal('0.00'))
        self.assertEqual(account.points, 10)

    def test_cadastrar_conta_poupanca(self):
        account = Account.objects.create(number=35791, account_type='poupanca')
        self.assertEqual(account.account_type, 'poupanca')
        self.assertEqual(account.balance, Decimal('0.00'))

    def test_consultar_conta_normal(self):
        account = Account.objects.get(number=self.normal_account.number)
        self.assertEqual(account.account_type, 'normal')

    def test_consultar_conta_bonus(self):
        account = Account.objects.get(number=self.bonus_account.number)
        self.assertEqual(account.account_type, 'bonus')

    def test_consultar_conta_poupanca(self):
        account = Account.objects.get(number=self.poupanca_account.number)
        self.assertEqual(account.account_type, 'poupanca')

    def test_consultar_saldo(self):
        balance = self.normal_account.balance
        self.assertEqual(balance, Decimal('100.00'))

    def test_credito_normal(self):
        value = Decimal('50.00')
        self.normal_account.balance += value
        self.normal_account.save()
        self.assertEqual(self.normal_account.balance, Decimal('150.00'))

    def test_credito_valor_negativo(self):
        value = Decimal('-50.00')
        self.assertRaises(ValueError, self.normal_account.balance.__add__, value)

    def test_credito_bonus(self):
        value = Decimal('100.00')
        self.bonus_account.balance += value
        self.bonus_account.points += int(value / 100)
        self.bonus_account.save()
        self.assertEqual(self.bonus_account.balance, Decimal('300.00'))
        self.assertEqual(self.bonus_account.points, 2)

    def test_debito_normal(self):
        value = Decimal('50.00')
        self.normal_account.balance -= value
        self.normal_account.save()
        self.assertEqual(self.normal_account.balance, Decimal('50.00'))

    def test_debito_valor_negativo(self):
        value = Decimal('-50.00')
        self.assertRaises(ValueError, self.normal_account.balance.__sub__, value)

    def test_debito_saldo_insuficiente_normal(self):
        value = Decimal('200.00')
        self.assertRaises(ValueError, self.normal_account.balance.__sub__, value)

    def test_debito_saldo_insuficiente_poupanca(self):
        value = Decimal('600.00')
        self.assertRaises(ValueError, self.poupanca_account.balance.__sub__, value)

    def test_transferencia_valor_negativo(self):
        value = Decimal('-50.00')
        self.assertRaises(ValueError, self.normal_account.balance.__sub__, value)

    def test_transferencia_saldo_insuficiente(self):
        source_balance = self.normal_account.balance
        destination_balance = self.bonus_account.balance
        value = Decimal('200.00')
        self.assertRaises(ValueError, self.normal_account.balance.__sub__, value)
        self.assertEqual(self.normal_account.balance, source_balance)
        self.assertEqual(self.bonus_account.balance, destination_balance)

    def test_transferencia_bonus(self):
        source_balance = self.bonus_account.balance
        destination_balance = self.normal_account.balance
        value = Decimal('100.00')

        self.bonus_account.balance -= value
        self.normal_account.balance += value
        self.normal_account.points += int(value / 200)
        self.bonus_account.save()
        self.normal_account.save()

        self.assertEqual(self.bonus_account.balance, source_balance - value)
        self.assertEqual(self.normal_account.balance, destination_balance + value)
        self.assertEqual(self.normal_account.points, 0)

    def test_render_juros_poupanca(self):
        interest_rate = Decimal('0.05')
        current_balance = self.poupanca_account.balance

        interest_amount = current_balance * (interest_rate / 100)
        self.poupanca_account.balance += interest_amount
        self.poupanca_account.save()

        self.assertEqual(self.poupanca_account.balance, current_balance + interest_amount)

       
