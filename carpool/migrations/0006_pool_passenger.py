# Generated by Django 2.2.2 on 2019-07-02 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0005_pool_tot'),
    ]

    operations = [
        migrations.AddField(
            model_name='pool',
            name='passenger',
            field=models.BooleanField(default=True),
        ),
    ]
