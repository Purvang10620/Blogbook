# Generated by Django 3.1.1 on 2021-03-05 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0006_blogtemplate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogtemplate',
            name='templatename',
            field=models.CharField(max_length=200),
        ),
    ]