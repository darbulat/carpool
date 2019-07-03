# Generated by Django 2.2.2 on 2019-07-03 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0011_auto_20190703_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pool',
            name='amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='pool',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17),
        ),
    ]
