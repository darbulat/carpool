# Generated by Django 2.2.2 on 2019-07-13 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carpool', '0022_pool_vk_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pool',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
