# Generated by Django 3.0.8 on 2020-07-23 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_auto_20200723_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True, verbose_name='active'),
        ),
    ]
