from django.db import models
from django.conf import settings
from DietPlanApp.models import DietPlan
# Create your models here.
class FitnessPlan(models.Model):
    coach = models.ForeignKey(DietPlan, on_delete=models.CASCADE, related_name='fitness_plans')
    title = models.CharField(max_length=200)
    workout_type = models.CharField(max_length=100)


