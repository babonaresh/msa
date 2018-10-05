from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class School(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    contact_person = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='school_created_by')

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name


class Player(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=1)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    eligibility_status = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player_created_by')
    updated_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='player_updated_by')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='player_school')

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.first_name + self.last_name


class Field(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    postal_code = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    notes = models.TextField()
    contact_person = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='field_created_by')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='school_field')

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name