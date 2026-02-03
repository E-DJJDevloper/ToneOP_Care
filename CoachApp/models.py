from django.db import models

# Create your models here.
from django.db import models
from UserAc.models import MyUser

class Coach(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)