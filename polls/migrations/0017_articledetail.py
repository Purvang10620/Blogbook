# Generated by Django 3.1.1 on 2021-03-16 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0016_delete_articledetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='articleDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('articleName', models.CharField(max_length=200)),
                ('article', models.TextField()),
                ('articleCatagories', models.CharField(max_length=100)),
                ('articleImage', models.ImageField(upload_to='profiles')),
                ('articleKeyword', models.CharField(max_length=200)),
                ('articleDate', models.DateField(default=django.utils.timezone.now)),
                ('articleAuthor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('blogAssociated', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='polls.blogdetails')),
            ],
        ),
    ]
