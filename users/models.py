from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Unit(models.Model):
    units = models.CharField(max_length=50)

    def __str__(self):
        return self.units


class UnitHead(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True, null=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='pics')
    
    def __str__(self):
        return f'{self.user.username} profile'