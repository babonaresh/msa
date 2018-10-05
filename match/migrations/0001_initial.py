# Generated by Django 2.0 on 2018-10-05 19:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('msa', '0002_field'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_day', models.DateField(default=django.utils.timezone.now)),
                ('match_start_time', models.TimeField()),
                ('match_end_time', models.TimeField()),
                ('home_team_score', models.IntegerField()),
                ('guest_team_score', models.IntegerField()),
                ('referee_comments', models.TextField()),
                ('status', models.CharField(choices=[('in_progress', 'In_Progress'), ('scheduled', 'Scheduled'), ('finished', 'Finished'), ('abandoned', 'Abandoned')], default='scheduled', max_length=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_field', to='msa.Field')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_score', models.IntegerField()),
                ('role', models.CharField(choices=[('none', 'None'), ('captain', 'Captain'), ('goalkeeper', 'Goal-Keeper')], default='None', max_length=10)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player_match', to='match.Match')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('logo', models.ImageField(blank=True, upload_to='teams/%Y/%m/%d')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Team_Coach', to=settings.AUTH_USER_MODEL)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='School_team', to='msa.School')),
            ],
        ),
        migrations.CreateModel(
            name='TeamPlayer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player', to=settings.AUTH_USER_MODEL)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='match.Team')),
            ],
        ),
        migrations.AddField(
            model_name='playermatch',
            name='team_player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_player_id', to='match.TeamPlayer'),
        ),
        migrations.AddField(
            model_name='match',
            name='guest_team_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Guest_team', to='match.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Home_team', to='match.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='referee_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_referee', to=settings.AUTH_USER_MODEL),
        ),
    ]
