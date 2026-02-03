from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import FitnessPlan
from .serializers import FitnessPlanSerializer

class IMember(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Member").exists()

class FitnessPlanViewSet(viewsets.ModelViewSet):
    queryset = FitnessPlan.objects.all()
    serializer_class = FitnessPlanSerializer
    permission_classes = [permissions.IsAuthenticated, IMember]

    def get_queryset(self):
        return FitnessPlan.objects.filter(user=self.request.user)