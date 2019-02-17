# Generated by Django 2.1.4 on 2019-02-14 23:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20190215_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='URL',
        ),
        migrations.AlterField(
            model_name='game',
            name='Rank1player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='game',
            name='Rank2player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player2', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='game',
            name='Rank3player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player3', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='game',
            name='game_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
