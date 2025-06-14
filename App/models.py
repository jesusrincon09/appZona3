from django.db import models
from enum import Enum
from django.contrib.auth.models import Permission
from django.contrib.auth import get_user_model

User = get_user_model()

class Sport(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True, max_length=1000)

    class Meta:
        verbose_name = 'Sport'
        verbose_name_plural = 'Sports'
        db_table = 'sport'
        default_permissions = ()

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='company_logo/', null=True, blank=True)

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'
        db_table = 'company'
        default_permissions = ()

    def __str__(self):
        return self.name

class Days(Enum):
    LUNES = 1
    MARTES = 2
    MIERCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SABADO = 6
    DOMINGO = 7

    @classmethod
    def choices(cls):
        return [(tag.value, tag.name.capitalize()) for tag in cls]

class Schedule(models.Model):
    day = models.IntegerField(choices=Days.choices(), default=Days.LUNES.value)
    startime = models.TimeField()
    endtime = models.TimeField()

    class Meta:
        verbose_name = 'Schedule'
        verbose_name_plural = 'Schedules'
        db_table = 'schedules'
        default_permissions = ()

    def __str__(self):
        return f"{Days(self.day).name} ({self.startime} - {self.endtime})"

    @property
    def day_name(self):
        return Days(self.day).name.capitalize()

    
class Spaces(models.Model):
    name = models.CharField(max_length=50)
    sport = models.ForeignKey(Sport, on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True)
    schedule = models.ManyToManyField(Schedule, blank=True)
    numberplayers = models.IntegerField()

    class Meta:
        verbose_name = 'Space'
        verbose_name_plural = 'Spaces'
        db_table = 'spaces'
        default_permissions = ()

    def __str__(self):
        return self.name

class Reservation(models.Model):
    client_name = models.CharField(max_length=50)
    client_cell = models.CharField(max_length=15)
    client_email = models.EmailField()
    space = models.ForeignKey(Spaces, on_delete=models.PROTECT)
    reservation_start = models.DateTimeField()
    reservation_end = models.DateTimeField()

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
        db_table = 'reservation'
        default_permissions = ()

    def __str__(self):
        return self.client_name

class Module(models.Model):
    name = models.CharField(max_length=100, unique=True)
    icon = models.CharField(max_length=50)
    permissions = models.ManyToManyField(Permission, related_name='modules')
    url_name = models.CharField(max_length=100) 

    class Meta:
        default_permissions = ()

    def __str__(self):
        return self.name

    def user_has_access(self, user):
        return user.user_permissions.filter(id__in=self.permissions.values_list('id', flat=True)).exists()



class Log(models.Model):
    ACTION_CHOICES = [
        ('create', 'Create'),
        ('update', 'Update'),
        ('delete', 'Delete'),
    ]

    module = models.CharField(max_length=255)  
    date = models.DateTimeField(auto_now_add=True)  
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)  
    description = models.TextField()  
    action = models.CharField(max_length=10, choices=ACTION_CHOICES) 

    def __str__(self):
        return f"{self.module} - {self.action} - {self.date.strftime('%Y-%m-%d %H:%M:%S')}"



















