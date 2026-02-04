from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import CoachPlanViewSet

# router = DefaultRouter()
# router.register(r'dietplans', CoachPlanViewSet, basename='dietplan')

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CoachPlanViewSet

router = DefaultRouter()
router.register(r'coaches', CoachPlanViewSet, basename='coach')

urlpatterns = [
    path('', include(router.urls)),
]