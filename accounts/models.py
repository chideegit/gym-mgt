from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta

class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    has_access = models.BooleanField(default=False)
    initial_payment = models.BooleanField(default=False)
    
class GymMembership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    next_sub_date = models.DateField(null=True)
    last_sub_date = models.DateField(null=True)

    def sub_date_calculations(self):
        last_payment = datetime.strptime(self.last_sub_date, "FORMAT")
        next_payment = last_payment + timedelta(days=31)
        return next_payment 