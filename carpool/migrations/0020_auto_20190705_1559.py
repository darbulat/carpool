# Generated by Django 2.2.2 on 2019-07-05 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0019_remove_pool_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pool',
            name='phone_number',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]