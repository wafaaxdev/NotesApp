# Generated by Django 3.1.2 on 2020-10-12 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201012_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='join_date',
            field=models.DateField(default=datetime.datetime(2020, 10, 12, 10, 52, 47, 155622)),
        ),
    ]