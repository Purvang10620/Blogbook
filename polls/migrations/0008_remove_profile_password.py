# Generated by Django 3.1.1 on 2021-03-07 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20210305_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='password',
        ),
    ]