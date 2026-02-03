from django.db import models
from django.conf import settings
# Create your models here.
from UserAc.models import MyUser

class Tracker(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    weight = models.FloatField()
    completed_workout = models.BooleanField(default=False)