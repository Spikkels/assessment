from django.db import models
from django.contrib.auth.models import User
from django.contrib.gis.db import models

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home_address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    location = models.PointField()

    def __str__(self):
        return self.user.username
