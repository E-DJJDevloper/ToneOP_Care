"""
URL configuration for ToneOP_Care project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('UserAc.urls')),
    path('coaches/', include('CoachApp.urls')),
    path('dietplans/', include('DietPlanApp.urls')),
    path('fitnessplans/', include('FitnessPlanApp.urls')),
    path('trackers/', include('UserTracker.urls')),
]

# from django.contrib import admin
# from django.urls import path, include
# from rest_framework import routers
# from UserAc.views import SignUpView, 
# from CoachApp.views import CoachViewSet
# from DietPlanApp.views import DietPlanViewSet
# from FitnessPlanApp.views import FitnessPlanViewSet
# from UserTracker.views import TrackerViewSet

# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'coaches', CoachViewSet)
# router.register(r'dietplans', DietPlanViewSet)
# router.register(r'fitnessplans', FitnessPlanViewSet)
# router.register(r'trackers', TrackerViewSet)

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include(router.urls)),
#     path('dashboard/', include('dashboard.urls')),
# ]

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),

#     # Only Coach and Tracker apps exposed at project level
#     path('coaches/', include('CoachApp.urls')),
#     path('trackers/', include('TrackerApp.urls')),
# ]