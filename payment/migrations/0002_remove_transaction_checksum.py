# Generated by Django 2.1.5 on 2019-01-13 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='checksum',
        ),
    ]
