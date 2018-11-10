from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class School(models.Model):
    ACTIVE_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    school_name = models.CharField(max_length=50)
    active_status = models.CharField(max_length=10, choices=ACTIVE_CHOICES, default='active')
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=10)
    contact_person = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.school_name)

class Field(models.Model):
    ACTIVE_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    school_name = models.ForeignKey(School, on_delete=models.CASCADE, related_name='field_school')
    field_name = models.CharField(max_length=50)
    active_status = models.CharField(max_length=10, choices=ACTIVE_CHOICES, default='active')
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=10)
    owner_org = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.field_name)

class Team(models.Model):
    ACTIVE_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    team_name = models.CharField(max_length=100)
    school = models.ForeignKey(School,on_delete=models.CASCADE, related_name='team_school')
    active_status = models.CharField(max_length=10, choices=ACTIVE_CHOICES, default='active')
    team_logo = models.ImageField(upload_to='team-logo/', blank=True, null=True)
    coach = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='team_coach', null=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.team_name)


class Match(models.Model):
    class Meta:
        verbose_name_plural = "matches"
    STATUS_CHOICES = (
        ('scheduled', 'Scheduled'),
        ('in_progress', 'In Progress'),
        ('full_time', 'Full Time'),
        ('cancelled', 'Cancelled'),
        ('abandoned', 'Abandoned'),
    )
    home_team = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name='match_home_team', null=True)
    guest_team = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name='match_guest_team', null=True)
    match_day = models.DateField(default=timezone.now)
    match_start_time = models.TimeField(default=timezone.now)
    match_end_time = models.TimeField(default=timezone.now)
    field = models.ForeignKey(Field, on_delete=models.SET_NULL, related_name='match_field', null=True)
    match_referee = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='match_referee', null=True)
    match_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='scheduled')
    home_team_score = models.IntegerField(null=True)
    guest_team_score = models.IntegerField(null=True)
    referee_comments = models.TextField(null=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.home_team) + ' vs ' + str(self.guest_team) + ' - ' + str(self.match_day)

class Player(models.Model):
    ELIGIBITY_CHOICES = (
        ('eligible', 'Eligible'),
        ('retired', 'Retired'),
        ('ineligible', 'Ineligible'),
        ('injured', 'Injured'),
    )
    ROLE_CHOICES = (
        ('captain', 'Captain'),
        ('vice_captain', 'Vice Captain'),
        ('none', 'None')
    )
    POSITION_CHOICES = (
        ('goalkeeper', 'Goalkeeper'),
        ('defender', 'Defender'),
        ('midfielder', 'Midfielder'),
        ('forward', 'Forward'),
    )
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=30)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='player_team')
    eligibility_status = models.CharField(max_length=20, choices=ELIGIBITY_CHOICES, default='eligible')
    team_role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='none')
    squad_position = models.CharField(max_length=20, choices=POSITION_CHOICES, default='forward')
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=10)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)


class Goal(models.Model):
    match = models.ForeignKey(Match, on_delete=models.SET_NULL, related_name='goal_match', null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name='goal_team', null=True)
    player = models.ForeignKey(Player, on_delete=models.SET_NULL, related_name='goal_player', null=True)
    goal_minute = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)