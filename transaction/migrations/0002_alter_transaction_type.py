# Generated by Django 5.0.1 on 2024-02-26 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.CharField(choices=[('Deposite', 'Deposite'), ('Purchase', 'Purchase')], max_length=255),
        ),
    ]
