# Generated by Django 5.0.1 on 2024-02-11 18:07

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0004_alter_book_language_alter_book_isbn_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('type', models.CharField(choices=[('Deposite', 'Deposite'), ('Purchase', 'Purchase')])),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='book.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]