# Generated by Django 3.1.2 on 2020-10-02 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0002_auto_20201002_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]