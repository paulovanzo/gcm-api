# Generated by Django 4.2.1 on 2023-05-21 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_account_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[('normal', 'Normal'), ('poupanca', 'Poupança')], default='normal', max_length=10),
        ),
    ]
