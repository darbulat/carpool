# Generated by Django 2.2.2 on 2019-06-28 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='phone',
        ),
    ]
