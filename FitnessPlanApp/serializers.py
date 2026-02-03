from rest_framework import serializers
from .models import FitnessPlan

class FitnessPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessPlan
        fields = '__all__'