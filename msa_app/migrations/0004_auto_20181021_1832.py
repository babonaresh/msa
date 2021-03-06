# Generated by Django 2.0.5 on 2018-10-21 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msa_app', '0003_auto_20181018_1921'),
    ]

    operations = [
        migrations.RenameField(
            model_name='field',
            old_name='contact',
            new_name='contact_person',
        ),
        migrations.RenameField(
            model_name='school',
            old_name='contact',
            new_name='contact_person',
        ),
        migrations.AddField(
            model_name='player',
            name='squad_position',
            field=models.CharField(choices=[('goalkeeper', 'Goalkeeper'), ('defender', 'Defender'), ('midfielder', 'Midfielder'), ('forward', 'Forward')], default='forward', max_length=20),
        ),
        migrations.AddField(
            model_name='player',
            name='team_role',
            field=models.CharField(choices=[('captain', 'Captain'), ('vice_captain', 'Vice Captain'), ('none', 'None')], default='none', max_length=20),
        ),
        migrations.AlterField(
            model_name='match',
            name='match_status',
            field=models.CharField(choices=[('scheduled', 'Scheduled'), ('in_progress', 'In Progress'), ('full_time', 'Full Time'), ('cancelled', 'Cancelled'), ('abandoned', 'Abandoned')], default='scheduled', max_length=20),
        ),
        migrations.AlterField(
            model_name='player',
            name='eligibility_status',
            field=models.CharField(choices=[('eligible', 'Eligible'), ('retired', 'Retired'), ('ineligible', 'Ineligible'), ('injured', 'Injured')], default='eligible', max_length=20),
        ),
    ]
