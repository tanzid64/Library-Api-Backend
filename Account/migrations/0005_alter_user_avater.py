# Generated by Django 5.0.1 on 2024-02-24 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_alter_user_avater'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avater',
            field=models.ImageField(default='./media/profile_picture/avater.jpg', upload_to='profile_picture/'),
        ),
    ]