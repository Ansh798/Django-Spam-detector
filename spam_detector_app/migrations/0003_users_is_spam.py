# Generated by Django 4.2 on 2023-08-01 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spam_detector_app', '0002_alter_users_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='is_spam',
            field=models.BooleanField(default=False),
        ),
    ]