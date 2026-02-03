from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Coach
from .serializers import CoachSerializer

class IsMember(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Member").exists()

class CoachPlanViewSet(viewsets.ModelViewSet):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer
    permission_classes = [permissions.IsAuthenticated, IsMember]

    def get_queryset(self):
        return Coach.objects.filter(user=self.request.user)