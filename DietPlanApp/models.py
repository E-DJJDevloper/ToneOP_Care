from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from CoachApp.models import Coach
class DietPlan(models.Model):
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE, related_name='diets')
    title = models.CharField(max_length=200)
    description = models.TextField()
    calories_target = models.IntegerField()