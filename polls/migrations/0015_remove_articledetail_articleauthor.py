# Generated by Django 3.1.1 on 2021-03-16 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_articledetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articledetail',
            name='articleAuthor',
        ),
    ]
