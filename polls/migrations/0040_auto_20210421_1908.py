# Generated by Django 3.1.1 on 2021-04-21 13:38

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0039_auto_20210419_1002'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='userProfile',
        ),
    ]
