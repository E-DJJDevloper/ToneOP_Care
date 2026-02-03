from django.shortcuts import render
# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, permissions
from .models import Tracker
from .serializers import TrackerSerializer

class Member(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name="Member").exists()

class TrackerPlanViewSet(viewsets.ModelViewSet):
    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer
    permission_classes = [permissions.IsAuthenticated, Member]

    def get_queryset(self):
        return Tracker.objects.filter(user=self.request.user)