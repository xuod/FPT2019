# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-01-13 19:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EternalRejection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Jury',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=50, verbose_name=b'Nom')),
                ('name', models.CharField(max_length=50, verbose_name=b'Pr\xc3\xa9nom')),
                ('affiliation', models.CharField(blank=True, max_length=100, verbose_name=b'Affiliation \xc3\xa0 afficher')),
                ('email', models.EmailField(help_text=b'Cette adresse sera utilis\xc3\xa9e pour envoyer des informations importantes aux jur\xc3\xa9s.', max_length=254, null=True, verbose_name=b'Email')),
                ('pf1', models.BooleanField(default=False, verbose_name=b'Pr\xc3\xa9sent lors du PF 1 ?')),
                ('pf2', models.BooleanField(default=False, verbose_name=b'Pr\xc3\xa9sent lors du PF 2 ?')),
                ('pf3', models.BooleanField(default=False, verbose_name=b'Pr\xc3\xa9sent lors du PF 3 ?')),
                ('pf4', models.BooleanField(default=False, verbose_name=b'Pr\xc3\xa9sent lors du PF 4 ?')),
                ('remark', models.TextField(blank=True, verbose_name=b'Remarques')),
            ],
        ),
        migrations.CreateModel(
            name='JuryGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_reporter', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=None)),
                ('grade_opponent', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=None)),
                ('jury', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FPT2019.Jury')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50, verbose_name=b'Pr\xc3\xa9nom')),
                ('surname', models.CharField(default=None, max_length=50, verbose_name=b'Nom')),
                ('gender', models.CharField(choices=[(b'M', b'Homme'), (b'F', b'Femme'), (b'D', b'Ne souhaite pas pr\xc3\xa9ciser')], max_length=1, verbose_name=b'Genre')),
                ('email', models.EmailField(help_text=b'Cette adresse sera utilis\xc3\xa9e pour envoyer des informations importantes aux participants.', max_length=254, verbose_name=b'Email')),
                ('birthdate', models.DateField(default=b'1900-01-31', verbose_name=b'Date de naissance')),
                ('role', models.CharField(choices=[(b'TM', b'Team Member'), (b'TC', b'Team Captain'), (b'TL', b'Team Leader'), (b'ACC', b'Accompagnant')], default=b'TM', help_text=b"L'\xc3\xa9quipe doit comporter exactement un Team Captain (\xc3\xa9tudiant), entre deux et cinq Team Members (\xc3\xa9tudiants) et entre un et deux Team Leaders (encadrants). N'oubliez pas de vous ajouter vous-m\xc3\xaame !", max_length=20, verbose_name=b'R\xc3\xb4le')),
                ('veteran', models.BooleanField(default=False, help_text=b"Est-ce que cette personne a d\xc3\xa9j\xc3\xa0 pris part au FPT ou \xc3\xa0 l'IPT ? (indicatif)", verbose_name=b'V\xc3\xa9t\xc3\xa9ran')),
                ('remark', models.TextField(blank=True, verbose_name=b'Remarques')),
                ('total_points', models.FloatField(default=0.0, editable=False)),
                ('mean_score_as_reporter', models.FloatField(default=0.0, editable=False)),
                ('mean_score_as_opponent', models.FloatField(default=0.0, editable=False)),
                ('tot_score_as_reporter', models.FloatField(default=0.0, editable=False)),
                ('tot_score_as_opponent', models.FloatField(default=0.0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=50)),
                ('description', models.CharField(default=None, max_length=500)),
                ('mean_score_of_reporters', models.FloatField(default=0.0, editable=False)),
                ('mean_score_of_opponents', models.FloatField(default=0.0, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_number', models.IntegerField(choices=[(1, b'Fight 1'), (2, b'Fight 2'), (3, b'Fight 3'), (4, b'Fight 4')], default=None)),
                ('round_number', models.IntegerField(choices=[(1, b'Round 1'), (2, b'Round 2')], default=None)),
                ('submitted_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('score_reporter', models.FloatField(default=0.0, editable=False)),
                ('score_opponent', models.FloatField(default=0.0, editable=False)),
                ('points_reporter', models.FloatField(default=0.0, editable=False)),
                ('points_opponent', models.FloatField(default=0.0, editable=False)),
                ('opponent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opponent_name', to='FPT2019.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='TacticalRejection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FPT2019.Problem')),
                ('round', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FPT2019.Round')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('total_points', models.FloatField(default=0.0, editable=False)),
                ('nrounds_as_rep', models.IntegerField(default=0, editable=False)),
                ('nrounds_as_opp', models.IntegerField(default=0, editable=False)),
                ('IOC', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Team_FPT2019', to=settings.AUTH_USER_MODEL, verbose_name=b'R\xc3\xa9f\xc3\xa9rent')),
            ],
        ),
        migrations.AddField(
            model_name='round',
            name='opponent_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opponentteam', to='FPT2019.Team'),
        ),
        migrations.AddField(
            model_name='round',
            name='problem_presented',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FPT2019.Problem'),
        ),
        migrations.AddField(
            model_name='round',
            name='reporter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reporter_name_1', to='FPT2019.Participant'),
        ),
        migrations.AddField(
            model_name='round',
            name='reporter_2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reporter_name_2', to='FPT2019.Participant'),
        ),
        migrations.AddField(
            model_name='round',
            name='reporter_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reporterteam', to='FPT2019.Team'),
        ),
        migrations.AddField(
            model_name='round',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FPT2019.Room'),
        ),
        migrations.AddField(
            model_name='participant',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FPT2019.Team', verbose_name=b'\xc3\x89quipe'),
        ),
        migrations.AddField(
            model_name='jurygrade',
            name='round',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FPT2019.Round'),
        ),
        migrations.AddField(
            model_name='jury',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='FPT2019.Team'),
        ),
        migrations.AddField(
            model_name='eternalrejection',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FPT2019.Problem'),
        ),
        migrations.AddField(
            model_name='eternalrejection',
            name='round',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='FPT2019.Round'),
        ),
    ]