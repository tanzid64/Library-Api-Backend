# Generated by Django 5.0.1 on 2024-02-15 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_user_is_publisher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_mod',
        ),
        migrations.AddField(
            model_name='user',
            name='address1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='address2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Addresses',
        ),
    ]
