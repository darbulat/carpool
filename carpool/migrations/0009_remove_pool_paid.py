# Generated by Django 2.2.2 on 2019-07-03 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0008_auto_20190702_2042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pool',
            name='paid',
        ),
    ]
