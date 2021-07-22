# Generated by Django 3.1.1 on 2021-03-22 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0019_usersociallink'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentBy', models.CharField(max_length=100)),
                ('commentbyEmail', models.CharField(max_length=100)),
                ('commentMsg', models.CharField(max_length=200)),
                ('commentOn', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.blogdetails')),
            ],
        ),
    ]