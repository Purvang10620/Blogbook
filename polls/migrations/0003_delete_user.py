# Generated by Django 3.1.1 on 2021-02-25 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210223_1630'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
