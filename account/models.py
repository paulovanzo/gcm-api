from django.db import models
from decimal import Decimal

class Account(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('normal', 'Normal'),
        ('bonus', 'Bônus'),
        ('poupanca', 'Poupança'),
    ]

    number = models.IntegerField(unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES, default='normal')
    points = models.IntegerField(default=0)

    def __str__(self):
        return str(self.number)

    def view_balance(self):
        return self.balance

    def credit(self, value):
        if value < 0:
            raise ValueError("Valor inválido")
        self.balance += value

        if self.account_type == 'bonus':
            self.points += int(value / 100)

        self.save()

    def debit(self, value):
        if value < 0:
            raise ValueError("Valor inválido")

        if self.account_type == 'poupanca':
            if self.balance >= value:
                self.balance -= value
                self.save()
            else:
                raise ValueError("Saldo insuficiente")
        else:
            if self.balance >= value - 1000:
                self.balance -= value
                self.save()
            else:
                raise ValueError("Saldo negativo ultrapassa -1000")

    def transfer(self, destination_account, value):
        if value < 0:
            raise ValueError("Valor inválido")
        if self.balance < value:
            raise ValueError("Conta de origem não possui saldo suficiente")
        
        self.balance -= value
        destination_account.balance += value

        if destination_account.account_type == 'bonus':
            destination_account.points += int(value / 200)

        self.save()
        destination_account.save()

    def yield_interest(self, interest_rate):
        if self.account_type != 'poupanca':
            raise ValueError("Apenas contas do tipo Poupança rendem juros")

        interest_amount = self.balance * (interest_rate / 100)
        self.balance += interest_amount
        self.save()

    @classmethod
    def create_account(cls, number, account_type, initial_balance=0):
        account = cls(number=number, account_type=account_type)

        if account.account_type == 'bonus':
            account.points += 10

        if account.account_type == 'poupanca':
            account.balance = initial_balance

        account.save()
        return account
