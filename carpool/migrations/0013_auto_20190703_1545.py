# Generated by Django 2.2.2 on 2019-07-03 07:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0012_auto_20190703_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pool',
            name='dateTime',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]