from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from msa.models import School, Field, Player


class Team(models.Model):
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='teams/%Y/%m/%d', blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)
    coach = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Team_Coach')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='School_team')

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Match(models.Model):
    STATUS_CHOICES = (
        ('in_progress', 'In_Progress'),
        ('scheduled', 'Scheduled'),
        ('finished', 'Finished'),
        ('abandoned', 'Abandoned'),
    )
    match_day = models.DateField(default=timezone.now)
    match_start_time = models.TimeField()
    match_end_time = models.TimeField()
    home_team_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='Home_team')
    guest_team_id = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='Guest_team')
    home_team_score = models.IntegerField()
    guest_team_score = models.IntegerField()
    referee_comments = models.TextField()
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='scheduled')

    created_date = models.DateTimeField(default=timezone.now)
    referee_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='match_referee')
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='match_field')

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.match_day) + str(self.home_team_id)


class TeamPlayer(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team')

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.player) + str(self.team)


class PlayerMatch(models.Model):
    Role_choices = (
        ('none', 'None'),
        ('captain', 'Captain'),
        ('goalkeeper', 'Goal-Keeper'),
    )

    team_player = models.ForeignKey(TeamPlayer, on_delete=models.CASCADE, related_name='team_player_id')
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='player_match')
    player_score = models.IntegerField()
    role = models.CharField(max_length=10,
                              choices=Role_choices,
                              default='None')
    created_date = models.DateTimeField(default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.team_player) + str(self.player_score)

