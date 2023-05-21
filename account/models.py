from django.db import models

class Account(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('normal', 'Normal'),
        ('bonus', 'Bônus'),
    ]

    number = models.IntegerField(unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES, default='normal')
    points = models.IntegerField(default=0)

    def __str__(self):
        return str(self.number)