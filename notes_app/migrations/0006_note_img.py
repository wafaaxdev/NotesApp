# Generated by Django 3.1.2 on 2020-10-09 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0005_auto_20201002_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='img',
            field=models.ImageField(default=' ', upload_to='notes-img'),
            preserve_default=False,
        ),
    ]