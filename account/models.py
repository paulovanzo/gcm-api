from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField(unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    class Meta:
        app_label = 'account'

    def __str__(self):
        return str(self.number)