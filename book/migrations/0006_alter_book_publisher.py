# Generated by Django 5.0.1 on 2024-02-16 13:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_book_price'),
        ('publisher', '0002_remove_publisher_is_approved_publisher_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(limit_choices_to={'is_publisher': True}, on_delete=django.db.models.deletion.CASCADE, related_name='book', to='publisher.publisher'),
        ),
    ]
