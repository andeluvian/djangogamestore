# Generated by Django 2.1.5 on 2019-01-22 13:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_remove_transaction_checksum'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
