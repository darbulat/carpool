# Generated by Django 2.1.1 on 2018-09-15 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0002_pool'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pool',
            name='amount',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
