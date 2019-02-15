# Generated by Django 2.1.4 on 2019-02-15 00:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0013_auto_20190215_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Highscore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('score',),
            },
        ),
        migrations.RemoveField(
            model_name='game',
            name='Rank1player',
        ),
        migrations.RemoveField(
            model_name='game',
            name='Rank1pts',
        ),
        migrations.RemoveField(
            model_name='game',
            name='Rank2player',
        ),
        migrations.RemoveField(
            model_name='game',
            name='Rank2pts',
        ),
        migrations.RemoveField(
            model_name='game',
            name='Rank3player',
        ),
        migrations.RemoveField(
            model_name='game',
            name='Rank3pts',
        ),
        migrations.AddField(
            model_name='game',
            name='highscores',
            field=models.ManyToManyField(to='store.Highscore'),
        ),
    ]
